from django.urls import path, include
from market.views import (
    index, 
    order_detail, 
    order_create, 
    product_create, 
    product_detail, 
    product_update, 
    product_ready, 
    ProductListView, 
    OrderListView
)
#, OrderCreateAPIView, OrderDetailAPIView, ProductUpdateAPIView

urlpatterns = [
    path('<int:pk>/index/', index, name="index"),
    path('farmer/product/', product_create, name="product"),
    path('retailer/order/', order_create, name="order"),
    path('farmer/product/list/', ProductListView.as_view(), name="product_list"),
    path('retailer/order/list/', OrderListView.as_view(), name="order_list"),
    path('product/ready/<int:pk>/', product_ready, name="ready"),
    path('retailer/order/detail/<int:pk>/', order_detail, name="detail"),
    path('product/detail/<int:pk>/', product_detail, name="details"),
    path('farmer/update/<int:pk>/', product_update, name="update"),
]
