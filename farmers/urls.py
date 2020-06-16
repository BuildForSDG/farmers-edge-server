
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('farmers.api.users.urlss')),
    path('api/v1/', include('farmers.api.contacts.urls')),
    path('auth/v1/', include('farmers.api.users.urls')),
    path('api/v1/', include('farmers.api.market.urls')),
    path('', include('farmers.api.users.reset_urls')),
    path('admin/', admin.site.urls),
]
