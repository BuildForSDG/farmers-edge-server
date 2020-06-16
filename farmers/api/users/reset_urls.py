from django.conf.urls import url,include 


urlpatterns = [
    url(r'^api/password_reset/', include('django_rest_passwordreset.urls')),
]