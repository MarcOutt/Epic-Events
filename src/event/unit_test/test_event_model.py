import pytest
from contract.models import Contract
from customer.models import Customer
from event.models import Event
from user.models import CustomUser


@pytest.mark.django_db
def test_create_customer():
    sales_contact = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                   first_name='Paul',
                                                   last_name='Laroche',
                                                   role='sale',
                                                   password='test_password')

    support_contact = CustomUser.objects.create_user(email='p.larose@example.com',
                                                     first_name='Pierre',
                                                     last_name='Larose',
                                                     role='support',
                                                     password='test_password')

    customer = Customer.objects.create(
        first_name='Pascal',
        last_name='Martin',
        email='p.martin@intel.com',
        phone='1234567890',
        mobile='0987654321',
        company_name='Intel',
        sales_contact=sales_contact
    )

    contract = Contract.objects.create(
        sales_contact=sales_contact,
        customer=customer,
        status=True,
        amount=350,
        payment_due="2023-04-22T18:12:00Z"
    )

    event = Event.objects.create(
        customer=customer,
        contract=contract,
        support_contact=support_contact,
        event_ended=True,
        attendees=30,
        event_date="2023-04-22T18:12:00Z",

    )
    assert event.support_contact == support_contact
    assert event.contract == contract
    assert event.event_ended == True
    assert event.event_date == "2023-04-22T18:12:00Z"
