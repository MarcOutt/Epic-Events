import pytest
from contract.models import Contract
from customer.models import Customer
from user.models import CustomUser


@pytest.mark.django_db
def test_create_customer():
    # create a sales contact user for the customer
    sales_contact = CustomUser.objects.create_user(email='p.laroche@example.com',
                                                   first_name='Paul',
                                                   last_name='Laroche',
                                                   role='sale',
                                                   password='test_password')

    # create a customer
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

    assert contract.sales_contact == sales_contact
    assert contract.customer == customer
    assert contract.status == True
    assert contract.payment_due == "2023-04-22T18:12:00Z"
