from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    SerializerMethodField,
    ValidationError
    )

User = get_user_model()
from users.models import Account

class UserLoginSerializer(ModelSerializer):
    
    email = EmailField(label='Email Address')
    class Meta:
        model = Account
        fields = [
            'email',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        password = data["password"]
        if not email:
            raise ValidationError("An email is required to login")
        
        user = Account.objects.filter (
                Q(email=email)
            ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")
            
        return data
