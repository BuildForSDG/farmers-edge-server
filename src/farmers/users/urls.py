from django.urls import path,include
from .api import RegisterAPI,LoginAPI,UserAPI,ActivateToken
from .views import activate_account
from knox import views as knox_views
urlpatterns = [
    path('api/auth/',include('knox.urls')),
    path('v1/register/',RegisterAPI.as_view(),name="register"),
    path('v1/login/',LoginAPI.as_view(),name="login"),
    path('v1/user/',UserAPI.as_view(),name="user_api"),
    path('v1/activate/<uidb64>/<token>',activate_account,name="activate"),
    # path('v1/logout/',knox_LogoutView.as_view())
    path('v1/logout/',knox_views.LogoutView.as_view(),name="logout"),
    path('api/auth/',include('knox.urls')),
]