import pytest
from customer.models import Customer
from customer.unit_test.customer_fixtures import get_tokens_for_user, management_user, sale_user, support_user, client
from rest_framework import status


@pytest.mark.django_db
def test_get_customers(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    response = client.get('/customers/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_user_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 1}

    response = client.post('/customers/', data=data)

    assert response.status_code == status.HTTP_201_CREATED

    customer = Customer.objects.get(email=data['email'])
    assert customer.first_name == data['first_name']
    assert customer.last_name == data['last_name']
    assert customer.phone == data['phone']


@pytest.mark.django_db
def test_create_user_with_management_user(client, management_user, sale_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 2}

    response = client.post('/customers/', data=data)
    print(response.request)
    assert response.status_code == status.HTTP_201_CREATED



@pytest.mark.django_db
def test_create_user_with_support_user(client, support_user):
    refresh_token = get_tokens_for_user(support_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 2}

    response = client.post('/customers/', data=data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_create_user_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 1}

    client.post('/customers/', data=data)

    data_update = {'first_name': 'Pascaline'}

    response = client.patch('/customers/1/', data=data_update)

    assert response.status_code == status.HTTP_200_OK

    customer = Customer.objects.get(email=data['email'])
    assert customer.first_name == data_update['first_name']


@pytest.mark.django_db
def test_update_customer_with_sale_user_but_is_not_sale_contact(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 2}

    client.post('/customers/', data=data)

    data_update = {'first_name': 'Pascaline'}

    response = client.patch('/customers/1/', data=data_update)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_delete_customer_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 1}

    client.post('/customers/', data=data)

    response = client.delete('/customers/1/')

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_customer_with_management_user(client, management_user, sale_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': 2}

    client.post('/customers/', data=data)

    response = client.delete('/customers/1/')

    assert response.status_code == status.HTTP_204_NO_CONTENT
