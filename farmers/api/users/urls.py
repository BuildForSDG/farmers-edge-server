from django.urls import path,include
from django.conf.urls import url
from .api import (
    RegisterAPI,
    LoginAPI,
    UserAPI,
    ActivateToken,
    PasswordResetRequest,
    ConfirmPasswordChange
)
from .views import activate_account,confirm_update
from knox import views as knox_views

urlpatterns = [
    path('api/auth/',include('knox.urls')),
    path('register/',RegisterAPI.as_view(),name="register"),
    path('login/',LoginAPI.as_view(),name="login"),
    path('user/',UserAPI.as_view(),name="user_api"),
    path('request/',PasswordResetRequest.as_view(),name="password_req"),
    # path('confirm/<uidb64>/token',confirm_update,name="confirm"),
    path('activate/<uidb64>/<token>',activate_account,name="activate"),
    path('api/password_reset/',include('django_rest_passwordreset.urls')),
    path('logout/',knox_views.LogoutView.as_view(),name="logout"),
]
