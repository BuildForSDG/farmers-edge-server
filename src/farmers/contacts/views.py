from django.shortcuts import render
from rest_framework import generics

from .models import Contact
from .serializers import ContactSerializer
from .tasks import send_issue_tracking_task
# Create your views here.

class ContactCreate(generics.CreateAPIView):
    queryset = Contact
    serializer_class = ContactSerializer
    def perform_create(self, serializer):
        name = self.request.data['name']
        email = self.request.data['email']
        subject = self.request.data['subject']
        message = self.request.data['message']
        send_issue_tracking_task.delay(name, email)
        serializer.save(name=name, email=email, subject=subject, message=message)


