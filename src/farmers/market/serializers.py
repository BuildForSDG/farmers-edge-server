from rest_framework import serializers
from market.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'retailer_email', 'product', 'totalCost', 'quantity', 'ready']
                     
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'productName', 'totalCost', 'quantity', 'waitTime']
                
