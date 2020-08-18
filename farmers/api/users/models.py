from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):

    USER_TYPE = (
        ('farmer', 'Farmer'),
        ('customer', 'Customer')
    )
    firstName = models.CharField(_('first name'), max_length=150)
    surname = models.CharField(_('surname'), max_length=150)
    email = models.EmailField(_('email'), unique=True)
    location = models.CharField(max_length=150)
    typeUser = models.CharField(max_length=150, choices=USER_TYPE, default='farmer')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return "{0} {1}".format(self.firstName, self.surname)
