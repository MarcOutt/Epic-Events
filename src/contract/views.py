
from contract.models import Contract
from contract.serializers import ContractSerializer
from crm.permissions import IsSale, IsSupport, IsManagement
from rest_framework import viewsets


class ContractViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""
    permission_classes = [IsManagement]
    serializer_class = ContractSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return Contract.objects.filter(customer_id=customer_id)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsSale, IsSupport]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSale]
        return [permission() for permission in permission_classes]