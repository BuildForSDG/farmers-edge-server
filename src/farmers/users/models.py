from django.db import models
# from django.auth.contib.models import Abstractuser
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(AbstractUser):
#     surname = models.CharField(max_length=25)
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email'), unique=True)
    full_name = models.CharField(_('full_name'),max_length=150)
    image = models.ImageField(upload_to="user_image", null=True, blank=True,default=0)
    phone_number = models.CharField(max_length=50)
    id_number = models.PositiveIntegerField(null=True)
    Location = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return "{0} {1} {2}".format(self.first_name,self.last_name,self.surname)