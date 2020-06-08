import pytest
from contacts.models import Contacts
from django.urls import reverse

@pytest.mark.django_db
def test_create_contact(client):
    data = {
        'name':'manu',
        'email':"emmanuelthedeveloper@gmail.com",
        'subject':'man',
        'message':'hey there'
    }
    url = reverse('contact_create')
    response = client.post(url,data)
    assert response.status_code == 200