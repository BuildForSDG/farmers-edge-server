from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

#Get all the created products
class ProductListView(ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        """
        This view should return a list of all the products
        for the currently authenticated user.
        """
        user = self.request.user
        return Product.objects.filter(user=user)

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """check if product is ready"""
        data = self.request.data              
        device = serializer.save()
        t = device.id
        # print(t)
        product = Product.objects.get(pk=t)
        if product.ready == True:
            print("email should be sent")
            x = Product.objects.get(pk=t)
            send_to = x.retailerEmail
            #print(x.retailer)
            subject = "Farmers Edge"
            message = "Dear Customer, Your order is ready. Please vist our website to process it. Thank you."
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [send_to], fail_silently=False)

@api_view(['PUT', ])
def product_update(request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "PUT":
            serializer = ProductSerializer(product, data=request.data)
            if product.ready == True:
                t = Product.objects.get(pk=pk)
                send_to = t.retailer_email
                print(t.retailer_email)
                subject = "Farmers Edge"
                message = "Dear Customer, Your order is ready. Please vist our website to process it. Thank you."
                from_email = settings.EMAIL_HOST_USER
                send_mail(subject, message, from_email, [send_to], fail_silently=False)

            data = {}
            if serializer.is_valid():
                    serializer.save()
                    data["success"] = "Product was Updataed Successfully"
                    return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get all the created orders
class OrderListView(ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def index(response, pk):
	ls = Product.objects.get(pk=pk)
	t = Order.objects.get(pk=5)
	print(t.retailer)
	print(ls.product)
	return HttpResponse("<h1>%s</h1>" %ls.farmer)
