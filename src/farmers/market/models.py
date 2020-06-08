from django.db import models
from django.utils import timezone
from django.conf import settings

class Product(models.Model):
    #farmer = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, null=True)
    totalCost = models.CharField(max_length=100, null=True)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.product

class Order(models.Model):
    productName = models.CharField(max_length=100, null=True)
    totalCost = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100, null=True)
    waitTime = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.productName

    # @property
    # def get_total(self):
    # 	total = self.product.price * self.quantity
    # 	return total
