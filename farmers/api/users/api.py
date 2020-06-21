from rest_framework.response import Response
from .models import User
from rest_framework import generics,permissions
from rest_framework.views import APIView
from knox.models import AuthToken
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    LoginSerializer,
    PasswordResetSerializer,
    ConfirmPasswordResetSerializer
    )
from .emails import send_welcome_email
from .tasks import send_confirmation_email_task,send_password_reset_token_task
from .token_generator import account_activation_token
from .reset_generator import reset_password

from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import HTMLFormRenderer,TemplateHTMLRenderer
from django.conf import settings

class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self,request,*args,**kwargs):
        """
        Handle user register
        """        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.email)
        token = AuthToken.objects.create(user)[1]
        b = request.get_host()
        # send_confirmation_email_task.delay(
        send_confirmation_email_task(
            user.username,
            user.email,
            urlsafe_base64_encode(force_bytes(user.pk)),
            b,
            account_activation_token.make_token(user)
        )
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": token
        })

class LoginAPI(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user)
        # import pdb; pdb.set_trace()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    def get_object(self):
        print(self.request.user)
        us = self.request.user
        return us

class ActivateToken(APIView):
    def get(self,*args,**kwargs):
        # print(**kwargs)
        return HttpResponse({"hey man"})
    def post(self):
        print("hey")
        return HttpResponse({"hey man"})

class PasswordResetRequest(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer
    
    def post(self,request,*args,**kwargs):
        # print(request.data['email'])
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        print(user)
        if email != user.email:
            print("this is not your account")
        else:
            b = request.get_host()
            # send_password_reset_token_task.delay(
            send_password_reset_token_task(
                user.username,
                user.email,
                urlsafe_base64_encode(force_bytes(user.pk)),
                b,
                account_activation_token.make_token(user)
            )
        return Response({"Received"})

class ConfirmPasswordChange(generics.CreateAPIView):
    serializer_class = ConfirmPasswordResetSerializer

    def post(self,request,*args,**kwargs):
        password = request.data['password']
        print(password)
        return Response({"hh"})
@api_view(['POST'])
def confirm_password_change(request,uidb64,token):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'change/pass_change.html'
    if request.method == 'POST':
        print('request.data')
        password = request.data['password']
        print(password)
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            print(user,token)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            print("usr",user)
            user.set_password(password)
            user.save()
            return Response({"You have reset your password successfully"})
        else:
            return Response({"Invalid token"})
        return Response("hey")
