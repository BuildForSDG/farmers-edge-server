from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):

    USER_TYPE = (
        ('farmer', 'Farmer'),
        ('customer', 'Customer')
    )
    username = models.CharField(_('username'),max_length=150)
    first_name = models.CharField(_('first name'),max_length=150)
    surname = models.CharField(_('surname'),max_length=150)
    email = models.EmailField(_('email'), unique=True)
    phone_number = models.CharField(_('phone number'), max_length=150)
    id_number = models.CharField(_('id number'), max_length=150)
    location = models.CharField(max_length=50)
    User_type = models.CharField(max_length=50, choices=USER_TYPE, default='farmer')
    image = models.ImageField(upload_to="user_image", null=True, blank=True,default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return "{0} {1}".format(self.first_name,self.surname)
