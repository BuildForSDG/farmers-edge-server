from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Product(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    retailerEmail = models.EmailField(max_length=254)
    product = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.product

class Order(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, null=True)
    waitTime = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.productName
