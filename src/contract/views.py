
from contract.models import Contract
from contract.serializers import ContractSerializer
from rest_framework import viewsets, serializers


class ContractViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""

    serializer_class = ContractSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return Contract.objects.filter(customer_id=customer_id)