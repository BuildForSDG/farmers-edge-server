from rest_framework import serializers
from market.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
                model = Product
                fields = ['product', 'total_cost', 'quantity', 'ready']
                
                
class OrderSerializer(serializers.ModelSerializer):
        class Meta:
                model = Order
                fields = ['product', 'total_cost', 'quantity', 'wait_time']
                
