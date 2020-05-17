from django.urls import path, include

from users.api import LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
    path('v1/user/', UserAPI.as_view(), name='user'),
    path('v1/login/', LoginAPI.as_view(), name="login"),
    path('v1/logout/',knox_views.LogoutView.as_view(),name="logout"),
]
