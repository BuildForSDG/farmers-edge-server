from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'retailerEmail', 'product', 'totalCost', 'quantity', 'ready']
                     
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'productName', 'totalCost', 'quantity', 'waitTime']
                
