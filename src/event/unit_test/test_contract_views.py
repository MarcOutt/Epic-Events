import pytest
from contract.models import Contract
from customer.models import Customer
from customer.unit_test.customer_fixtures import get_tokens_for_user, management_user, sale_user, support_user, client
from rest_framework import status


@pytest.mark.django_db
def test_get_contract_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )

    response = client.get(f'/customers/{customer.id}/contracts/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_customer_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )
    data = {
        'sales_contact': sale_user.id,
        'customer': customer.id,
        'status': True,
        'amount': 350,
        'payment_due': "2023-04-22T18:12:00Z"
    }

    response = client.post(f'/customers/{customer.id}/contracts/', data=data)
    contract = Contract.objects.get(amount=data['amount'])
    assert response.status_code == status.HTTP_201_CREATED
    assert contract.amount == data['amount']
    assert contract.status == data['status']


@pytest.mark.django_db
def test_update_customer_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )
    data = {
        'sales_contact': sale_user.id,
        'customer': customer.id,
        'status': True,
        'amount': 350,
        'payment_due': "2023-04-22T18:12:00Z"
    }

    response = client.post(f'/customers/{customer.id}/contracts/', data=data)
    contract_id = response.data['id']

    data_update = {'status': False}

    response = client.patch(f'/customers/{customer.id}/contracts/{contract_id}/', data=data_update)

    assert response.status_code == status.HTTP_200_OK

    contract = Contract.objects.get(amount=data['amount'])
    assert contract.status == data_update['status']


@pytest.mark.django_db
def test_delete_customer_with_sale_user(client, sale_user):
    refresh_token = get_tokens_for_user(sale_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )
    data = {
        'sales_contact': sale_user.id,
        'customer': customer.id,
        'status': True,
        'amount': 350,
        'payment_due': "2023-04-22T18:12:00Z"
    }

    response = client.post(f'/customers/{customer.id}/contracts/', data=data)
    contract_id = response.data['id']
    response = client.delete(f'/customers/{customer.id}/contracts/{contract_id}/')

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_customer_with_management_user(client, management_user, sale_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )
    data = {
        'sales_contact': sale_user.id,
        'customer': customer.id,
        'status': True,
        'amount': 350,
        'payment_due': "2023-04-22T18:12:00Z"
    }

    response = client.post(f'/customers/{customer.id}/contracts/', data=data)
    contract_id = response.data['id']
    response = client.delete(f'/customers/{customer.id}/contracts/{contract_id}/')

    assert response.status_code == status.HTTP_204_NO_CONTENT




