from rest_framework.response import Response
from .models import User
from rest_framework import generics,permissions
from rest_framework.views import APIView
from knox.models import AuthToken
from .serializers import RegisterSerializer,UserSerializer,LoginSerializer
from rest_framework.views import APIView
from .emails import send_welcome_email
from .tasks import send_confirmation_email_task
from .token_generator import account_activation_token


from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user.email)
        token = AuthToken.objects.create(user)[1]
        send_confirmation_email_task.delay(user.full_name,user.email,urlsafe_base64_encode(force_bytes(user.pk)),account_activation_token.make_token(user))
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token": token
        })
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user)
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