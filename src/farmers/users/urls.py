from django.urls import path,include
from django.conf.urls import url
from .api import RegisterAPI,LoginAPI,UserAPI,ActivateToken,PasswordResetRequest,ConfirmPasswordChange
from .views import activate_account,confirm_update
from knox import views as knox_views
urlpatterns = [
    path('api/auth/',include('knox.urls')),
    path('v1/register/',RegisterAPI.as_view(),name="register"),
    path('v1/login/',LoginAPI.as_view(),name="login"),
    path('v1/user/',UserAPI.as_view(),name="user_api"),
    path('v1/request/',PasswordResetRequest.as_view(),name="password_req"),
    # path('v1/confirm/<uidb64>/token',confirm_update,name="confirm"),
    path('v1/activate/<uidb64>/<token>',activate_account,name="activate"),
    path('v1/logout/',knox_views.LogoutView.as_view(),name="logout"),
    path('api/auth/',include('knox.urls')),
]
