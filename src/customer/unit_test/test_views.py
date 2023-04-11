import pytest
from customer.models import Customer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from user.models import CustomUser


User = get_user_model()

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


@pytest.fixture
def customer(user, client):
    return Customer.objects.create(first_name='Jean', last_name='Delacour', email='j.delacour@intel.com',
                                   phone='0160352703', mobile='0645873879', sales_contact=user.id)


@pytest.mark.django_db
def test_create_customer(client):
    response = client.post('/customers/', {
        'first_name': 'jean',
        'last_name': 'Delacour',
        'email': 'j.delacour@intel.com',
        'phone': '0160352703',
        'mobile': '0648253897',
        'company_name': 'intel',
        'sales_contact': '1'
    }, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_update_customer(client, user_data):
    user = CustomUser.objects.create_user(**user_data)
    customer = Customer.objects.create(first_name='Jean', last_name='Delacour', email='j.delacour@intel.com',
                                       phone='0160352703', mobile='0645873879', sales_contact=user.id)
    url = reverse('customer-detail', args=[customer.id])
    response = client.put(url, {
        'first_name': 'paul',
        'last_name': 'Delacour',
        'email': 'j.delacour@intel.com',
        'phone': '0160352703',
        'mobile': '0648253897',
        'company_name': 'intel',
        'sales_contact': user.id
    }, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_delete(customer, client):
    url = reverse('customer-detail', args=[customer.id])
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT



