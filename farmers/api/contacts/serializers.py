from rest_framework import serializers
from rest_framework.response import Response

from .models import Contact

#serializer here

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'name',
            'email',
            'subject',
            'message'
        )