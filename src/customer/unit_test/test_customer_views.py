import pytest
from customer.models import Customer
from customer.unit_test.customer_fixtures import get_tokens_for_user, management_user, sale_user, support_user, client
from rest_framework import status
from user.models import CustomUser


@pytest.mark.django_db
def test_get_customers(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')
    response = client.get('/customers/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_customer_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_contact = CustomUser.objects.create_user(email='p.blanche@example.com',
                                                   first_name='Pierre',
                                                   last_name='Blanche',
                                                   role='sale',
                                                   password='test_password')
    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': sales_contact.id}

    response = client.post('/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED

    customer = Customer.objects.get(email=data['email'])
    assert customer.first_name == data['first_name']
    assert customer.last_name == data['last_name']
    assert customer.phone == data['phone']


@pytest.mark.django_db
def test_create_customer_with_management_user(client, management_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_contact = CustomUser.objects.create_user(email='p.bleu@example.com',
                                                   first_name='Pierre',
                                                   last_name='Bleu',
                                                   role='sale',
                                                   password='test_password')
    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': sales_contact.id}

    response = client.post('/customers/', data=data)
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
def test_update_user_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': sale_user.id}

    response = client.post('/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
    costumer_id = response.data['id']

    data_update = {'first_name': 'Pascaline'}

    response = client.patch(f'/customers/{costumer_id}/', data=data_update)
    assert response.status_code == status.HTTP_200_OK

    customer = Customer.objects.get(email=data['email'])
    assert customer.first_name == data_update['first_name']


@pytest.mark.django_db
def test_update_customer_with_sale_user_but_is_not_sale_contact(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_contact = CustomUser.objects.create_user(email='p.rose@example.com',
                                                   first_name='Pierre',
                                                   last_name='rose',
                                                   role='sale',
                                                   password='test_password')
    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': sales_contact.id}

    response = client.post('/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
    costumer_id = response.data['id']

    data_update = {'first_name': 'Pascaline'}

    response = client.patch(f'/customers/{costumer_id}/', data=data_update)

    assert response.status_code == status.HTTP_403_FORBIDDEN


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
            'sales_contact': sale_user.id}

    response = client.post('/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
    costumer_id = response.data['id']

    response = client.delete(f'/customers/{costumer_id}/')

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_customer_with_management_user(client, management_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    sales_contact = CustomUser.objects.create_user(email='p.bleu@example.com',
                                                   first_name='Pierre',
                                                   last_name='Bleu',
                                                   role='sale',
                                                   password='test_password')
    data = {'first_name': 'Pascal',
            'last_name': 'Martin',
            'email': 'p.martin@intel.com',
            'phone': '1234567890',
            'mobile': '0987654321',
            'company_name': 'Intel.',
            'sales_contact': sales_contact.id}

    response = client.post('/customers/', data=data)
    assert response.status_code == status.HTTP_201_CREATED
    costumer_id = response.data['id']

    response = client.delete(f'/customers/{costumer_id}/')

    assert response.status_code == status.HTTP_204_NO_CONTENT



