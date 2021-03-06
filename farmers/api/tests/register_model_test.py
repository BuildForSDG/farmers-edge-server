import pytest
# from django.auth.model
from django.urls import reverse
import json
@pytest.mark.django_db
def test_register_user_model(django_user_model):
    user = django_user_model.objects.create(
       full_name="som", password='password',
       email='e@gmail.com',phone_number='+254740415950',
       id_number='34802334',Location="Kericho"
   )
    assert django_user_model.objects.count() == 1

#testing our api
@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()
@pytest.mark.django_db
def test_unauthorized_request(api_client):
    url = reverse('user_api')
    response = api_client.get(url)
    assert response.status_code == 401
@pytest.mark.django_db
def test_can_create_user(api_client):
    valid = {"full_name":"som",
     "password":'password',
     "email":'edeyghbjeedghbj@gmail.com',
     "phone_number":'+254740415950',
     "id_number":'34802334',
     "Location":"Kericho",
     "user_type":"FARMER"
     }
    url = reverse('register')
    response = api_client.post(url,valid
            )
    print("created")
    assert response.status_code == 200
import uuid
@pytest.fixture
def test_password():
   return 'strong-test-pass'
@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'email' not in kwargs:
           kwargs['email'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user
@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
   def make_auto_login(user=None):
       if user is None:
           user = create_user()
       client.login(email=user.email, password=test_password)
       return client, user
   return make_auto_login
@pytest.mark.django_db
def test_auth_view(auto_login_user):
   client, user = auto_login_user()
   url = reverse('user_api')
   response = client.get(url)
   assert response.status_code == 200
# @pytest.mark.django_db
# @pytest.mark.parametrize(
#    'email, password, status_code', [
#     #    (None, None, 400),
#     #    (None, 'strong_pass', 400),
#     #    ('user@example.com', None, 400),
#        ('user@example.com', 'invalid_pass', 400),
#        ('e@gmail.com', 'password', 200),
#    ]
# )
# def test_login_data_validation(
#    email, password, status_code, api_client,django_user_model
# ):
#    url = reverse('login')
#    data = {
#        'email': email,
#        'password': password
#    }
# #    api_client.force_authenticate(data)
# #    response = api_client.force_authenticate(data)
# #    response = api_client.login(email=email,password=password)
# #    print(response)
#    url1 = reverse('user_api')
#    response1 = api_client.post(url,{"username":"e@gmail.com","password":"password"})
#    assert response1.status_code == 400
#    api_client.logout()

# from contacts.models import Contacts
# from django.urls import reverse

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
    print(response)
    assert response.status_code == 201

