from django.urls import path, include
from market.views import (
    ProductCreateAPIView,
    ProductListView,
    OrderCreateAPIView,
    OrderListView,
    product_update
)

urlpatterns = [
    path('farmer/product/',  ProductCreateAPIView.as_view(), name="product"),
    path('retailer/order/', OrderCreateAPIView.as_view(), name="order"),
    path('farmer/product/list/', ProductListView.as_view(), name="product_list"),
    path('retailer/order/list/', OrderListView.as_view(), name="order_list"),
    path('farmer/update/<int:pk>/', product_update, name="update"),
]