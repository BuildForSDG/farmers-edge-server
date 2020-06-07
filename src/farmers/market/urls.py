from django.urls import path, include
from market.views import index, order_detail, order_create, product_create, product_detail, product_update, product_ready
#, OrderCreateAPIView, OrderDetailAPIView, ProductUpdateAPIView

urlpatterns = [
    path('<int:pk>/index/', index, name="index"),
    path('retailer/order/detail/<int:pk>/', order_detail, name="detail"),
    path('product/ready/<int:pk>/', product_ready, name="ready"),
    path('product/detail/<int:pk>/', product_detail, name="details"),
    path('farmer/update/<int:pk>/', product_update, name="update"),
    path('farmer/product/', product_create, name="product"),
    path('retailer/order/', order_create, name="order"),
]
