from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
