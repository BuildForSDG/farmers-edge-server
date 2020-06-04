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
from helpers.serial_errors import error_dict

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorect Credential")
        # return super().validate(attrs)

# register serializers
class RegisterSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    image = serializers.ImageField(default=None)
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'surname',
            'username',
            'email',
            'password',
            'phone_number',
            'location',
            'id_number',
            'User_type',
            'image'
        )
        extra_kwargs={'password':{'write_only':True}}


    def create(self, validated_data):
        # print(validated_data['image'])
        user = User.objects.create(
            first_name = validated_data['first_name'],
            surname = validated_data['surname'],
	        username = validated_data['username'],
            email = validated_data['email'],
            location = validated_data['location'],
            phone_number = validated_data['phone_number'],
            id_number = validated_data['id_number'],
            User_type = validated_data['User_type'],
            image = validated_data['image'],
            is_active = False
        )
        user.set_password(validated_data['password'])
        f = False
        user.is_active = False
        user.save()
        # print(user)
        # print(reverse('register'))
        return user

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'surname',
            'username',
            'email',
            'location',
            'phone_number',
            'id_number',
            'User_type',
            'image',
            'is_active'
        )
