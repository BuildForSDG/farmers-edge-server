from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.ContactCreate.as_view(),name="contact_create")
]