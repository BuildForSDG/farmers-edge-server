from rest_framework import serializers
from .models import User
from .emails import send_welcome_email
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.http import HttpResponse

class LoginSerializer(serializers.Serializer):
    """Serializes login requests and logs in registered user."""
    email = serializers.EmailField(default=None)
    password =  serializers.CharField(default=None)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorect Credential")
        # return super().validate(attrs)

# register serializers
class RegisterSerializer(serializers.ModelSerializer):
    """Serializes registration requests and creates a new user."""
    
    class Meta:
        model = User
        fields = (
            'id',
            'firstName',
            'surname',
            'username',
            'email',
            'password',
            'phoneNumber',
            'location',
            'idNumber',
            'typeUser',
        )
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        # print(validated_data['image'])
        user = User.objects.create(
            firstName = validated_data['firstName'],
            surname = validated_data['surname'],
	        username = validated_data['username'],
            email = validated_data['email'],
            location = validated_data['location'],
            phoneNumber = validated_data['phoneNumber'],
            idNumber = validated_data['idNumber'],
            typeUser = validated_data['typeUser'],
            is_active = False
        )
        user.set_password(validated_data['password'])
        f = False
        user.is_active = False
        user.save()
        # print(user)
        # print(reverse('register'))
        return user

class PasswordResetSerializer(serializers.ModelSerializer):
    """Serializes password reset requests."""
    
    class Meta:
        model = User
        fields = ('email',)

class ConfirmPasswordResetSerializer(serializers.ModelSerializer):
    """Serializes confirm password reset requests."""
    
    class Meta:
        model = User
        fields = ('password',)

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'firstName',
            'surname',
            'username',
            'email',
            'location',
            'phoneNumber',
            'idNumber',
            'typeUser',
            'is_active'
        )
