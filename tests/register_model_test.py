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
     "Location":"Kericho"
     }
    url = reverse('register')
    response = api_client.post(url,valid
            )
    assert response.status_code == 200

@pytest.mark.django_db
@pytest.mark.parametrize(
   'username, password, status_code', [
    #    (None, None, 400),
    #    (None, 'strong_pass', 400),
    #    ('user@example.com', None, 400),
       ('user@example.com', 'invalid_pass', 400),
       ('edeyghbjeedghbj@gmail.com', 'password', 200),
   ]
)
def test_login_data_validation(
   username, password, status_code, api_client
):
   url = reverse('login')
   data = {
       'username': username,
       'password': password
   }
   response = api_client.post(url, data=data)
   assert response.status_code == status_code
# @pytest.mark.django_db
# def test_user_login(api_client,django_user_model):
#     user = django_user_model.objects.create(
#         full_name="som", password='password',
#         email='e@gmail.com',phone_number='+254740415950',
#         id_number='34802334',Location="Kericho"
#     )
#     logs = {
#      "email":'e@gmail.com',
#      "password":'password'
#      }
#     url = reverse('login')
#     response = api_client.post(url,date = logs)
    # assert response.status_code == 400