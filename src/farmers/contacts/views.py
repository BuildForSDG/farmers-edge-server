from django.shortcuts import render
from rest_framework import generics

from .models import Contact
from .serializers import ContactSerializer
# Create your views here.

class ContactCreate(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSerializer

