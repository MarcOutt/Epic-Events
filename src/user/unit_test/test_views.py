from unittest.mock import patch

import pytest
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        'email': 'p.laroche@example.com',
        'first_name': 'Paul',
        'last_name': 'Laroche',
        'role': 'sale',
        'password': 'test_password',
    }


@pytest.fixture
def user(user_data):
    return CustomUser.objects.create_user(**user_data)


@pytest.mark.django_db
def test_create_user(user_data, client):
    response = client.post('/users/', user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

    # Check that the user was created with the correct data
    assert CustomUser.objects.count() == 1
    user = CustomUser.objects.first()
    assert user.email == user_data['email']
    assert user.first_name == user_data['first_name']
    assert user.last_name == user_data['last_name']
    assert user.role == user_data['role']
    assert user.check_password(user_data['password'])


@pytest.mark.django_db
def test_login(user_data, user):
    client = APIClient()
    url = reverse('login')
    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_login_failed(user_data, user, client):
    url = reverse('login')
    response = client.post(url, {'email': 'test@example.com', 'password': 'wrong_password'}, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Email ou mot de passe invalide' in response.data['error']


@pytest.mark.django_db
def test_user_update(user_data, user, client):
    url = reverse('user-detail', args=[user.id])
    response = client.put(url, {
        'email': 'p.laroche@example.com',
        'first_name': 'Paula',
        'last_name': 'Laroche',
        'role': 'sale',
        'password': 'test_password',
    }, format='json')
    assert response.status_code ==status.HTTP_200_OK
    assert response.data['first_name'] == 'Paula'



