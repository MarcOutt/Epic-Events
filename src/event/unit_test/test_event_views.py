import pytest
from contract.models import Contract
from customer.models import Customer
from customer.unit_test.customer_fixtures import get_tokens_for_user, management_user, sale_user, support_user, client
from event.models import Event
from rest_framework import status
from user.models import CustomUser


@pytest.mark.django_db
def test_get_event_with_sale_user(client, sale_user):
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

    contract = Contract.objects.create(
        sales_contact=sale_user,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    response = client.get(f'/customers/{customer.id}/contracts/{contract.id}/events/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_event_with_sale_user(client, management_user, sale_user):
    refresh_token = get_tokens_for_user(management_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    support_user = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                  first_name='Paul',
                                                  last_name='Laroche',
                                                  role='support',
                                                  password='test_password')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )

    contract = Contract.objects.create(
        sales_contact=sale_user,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    data = {
        'customer': customer.id,
        'contract': contract.id,
        'support_contact': support_user.id,
        'event_ended': False,
        'attendees': 30,
        'event_date': "2023-06-22T18:12:00Z",
        'notes': 'réserver un dj'
    }

    response = client.post(f'/customers/{customer.id}/contracts/{contract.id}/events/', data=data)
    print(response.content)
    assert response.status_code == status.HTTP_201_CREATED

    event = Event.objects.get(attendees=data['attendees'])
    assert event.notes == data['notes']


@pytest.mark.django_db
def test_update_event_with_support_user(client, sale_user):

    support_user = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                  first_name='Paul',
                                                  last_name='Laroche',
                                                  role='support',
                                                  password='test_password')

    refresh_token = get_tokens_for_user(support_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )

    contract = Contract.objects.create(
        sales_contact=sale_user,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    event = Event.objects.create(
        customer=customer,
        contract=contract,
        support_contact=support_user,
        event_ended=False,
        attendees=30,
        event_date="2023-04-22T18:12:00Z",

    )
    data_update = {'event_ended': True}

    response = client.patch(f'/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/', data=data_update)
    event_update = Event.objects.get(id=event.id)
    assert response.status_code == status.HTTP_200_OK
    assert event_update.event_ended == data_update['event_ended']


@pytest.mark.django_db
def test_delete_event_with_support_user(client, sale_user):

    support_user = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                  first_name='Paul',
                                                  last_name='Laroche',
                                                  role='support',
                                                  password='test_password')

    refresh_token = get_tokens_for_user(support_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh_token}')

    customer = Customer.objects.create(first_name='Pascal',
                                       last_name='Martin',
                                       email='p.martin@intel.com',
                                       phone='1234567890',
                                       mobile='0987654321',
                                       company_name='Intel',
                                       sales_contact=sale_user
                                       )

    contract = Contract.objects.create(
        sales_contact=sale_user,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    event = Event.objects.create(
        customer=customer,
        contract=contract,
        support_contact=support_user,
        event_ended=False,
        attendees=30,
        event_date="2023-04-22T18:12:00Z",

    )

    response = client.delete(f'/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/')
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_event_with_management_user(client, sale_user, management_user):

    support_user = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                  first_name='Paul',
                                                  last_name='Laroche',
                                                  role='support',
                                                  password='test_password')

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

    contract = Contract.objects.create(
        sales_contact=sale_user,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    event = Event.objects.create(
        customer=customer,
        contract=contract,
        support_contact=support_user,
        event_ended=False,
        attendees=30,
        event_date="2023-04-22T18:12:00Z",

    )

    response = client.delete(f'/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT