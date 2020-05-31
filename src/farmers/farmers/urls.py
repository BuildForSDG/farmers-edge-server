
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('users.urlss')),
    path('api/',include('contacts.urls')),
    path('auth/',include('users.urls')),
    path('api/v1/', include('market.urls')),
    path('',include('users.reset_urls')),
    path('auth/',include('users.urls')),
    path('admin/', admin.site.urls),
]
