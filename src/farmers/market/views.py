from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView


from market.models import Product, Order
from market.serializers import ProductSerializer, OrderSerializer
	


@api_view(['GET', ])
def product_detail(request, pk):
        
        try:
                product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
                serializer = ProductSerializer(product)
                return Response(serializer.data)


@api_view(['GET', ])
def order_detail(request, pk):
        
        try:
                order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
                serializer = OrderSerializer(order)
                return Response(serializer.data)


@api_view(['PUT', ])
def product_update(request, pk):
        
        try:
                product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "PUT":
                serializer = ProductSerializer(product, data=request.data)
                data = {}
                if serializer.is_valid():
                        serializer.save()
                        data["success"] = "Product was Updataed Successfully"
                        return Response(data=data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def product_ready(request, pk):
        
        try:
                product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
                serializer = ProductSerializer(product)
                if product.ready == True:
                	t = Order.objects.get(pk=pk)
                	send_to = t.retailer
                	subject = "Order is Ready"
                	message = "Your order is ready. Please vist the app to get more details"
                	from_email = settings.EMAIL_HOST_USER
                	send_mail(subject, message, from_email, [send_to], fail_silently=False)
                    #print('User should be emailed sent to')
                return Response(serializer.data)
                

@api_view(['POST', ])
def product_create(request):
	if request.method == "POST":
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def order_create(request):
	if request.method == "POST":
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def index(response, pk):
	ls = Product.objects.get(pk=pk)
	t = Order.objects.get(pk=5)
	print(t.retailer)
	print(ls.product)
	return HttpResponse("<h1>%s</h1>" %ls.farmer)

#Get all the created products
class ProductListView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


#Get all the created orders
class OrderListView(ListAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
                
