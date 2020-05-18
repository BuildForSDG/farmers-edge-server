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
    email = serializers.EmailField()
    password =  serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Incorect Credential")
        # return super().validate(attrs)


# register serializers
class RegisterSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default=None)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'full_name',
            'Location',
            'phone_number',
            'id_number',
            'image'
        )
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        # print(validated_data['image'])
        user = User.objects.create(
            full_name=validated_data['full_name'],
            email = validated_data['email'],
            Location = validated_data['Location'],
            phone_number = validated_data['phone_number'],
            image=validated_data['image'],
            id_number = validated_data['id_number'],
            is_active=False
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
            'username',
            'email',
            'Location',
            'full_name',
            'phone_number',
            'id_number',
            'image',
            'is_active'
        )