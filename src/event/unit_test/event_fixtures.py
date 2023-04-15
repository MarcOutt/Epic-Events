import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from user.models import CustomUser


@pytest.fixture
def client():
    return APIClient()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return refresh.access_token


@pytest.fixture
def management_user():
    return CustomUser.objects.create_user(email='r.lapierre@example.com',
                                          first_name='Robert',
                                          last_name='Lapierre',
                                          role='management',
                                          password='test_password')


@pytest.fixture
def sale_user():
    return CustomUser.objects.create_user(email='p.bleu@example.com',
                                          first_name='Pierre',
                                          last_name='Bleu',
                                          role='sale',
                                          password='test_password')


@pytest.fixture
def support_user():
    return CustomUser.objects.create_user(email='p.laroche@example.com',
                                          first_name='Paul',
                                          last_name='Laroche',
                                          role='support',
                                          password='test_password')
