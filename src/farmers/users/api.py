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
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self,request,*args,**kwargs):
        print("+=====", request.data)

        """
        Handle user register
        """        
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = AuthToken.objects.create(user)[1]

            send_confirmation_email_task.delay(
                user.surname,
                user.email,
                urlsafe_base64_encode(force_bytes(user.pk)),
                account_activation_token.make_token(user))

            data = {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            }

            return Response( 
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

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
