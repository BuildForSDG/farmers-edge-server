import json
from market.models import Product, Order
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from market.serializers import ProductSerializer, OrderSerializer




#     
class ProductViewTestCase(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(product="maziwa", total_cost="44", quantity="40kgs", ready=True)


    def test_product_list(self):
        response = self.client.get("/api/v1/product/detail/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_product_create(self):
        data = {"product": "ugali", "total_cost": "567", "quantity": "50 kgs", "ready": "true"}
        response = self.client.post("/api/v1/farmer/product/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_product_update(self):
        data = {"product": "ugali", "total_cost": "57", "quantity": "50 kgs", "ready": "false"}
        response = self.client.put("/api/v1/farmer/update/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        

class OrderViewTestCase(APITestCase):

    def setUp(self):
        # This order inherites from the product model
        self.order = Order.objects.create(total_cost="44", quantity="40kgs", wait_time="days")


    def test_order_list(self):
        response = self.client.get("/api/v1/retailer/order/detail/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_order_create(self):
        data = {"total_cost": "567", "quantity": "50 kgs", "wait_time": "days"}
        response = self.client.post("/api/v1/retailer/order/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
