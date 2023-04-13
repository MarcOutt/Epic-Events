
from contract.models import Contract
from contract.serializers import ContractSerializer
from crm.permissions import IsSale, IsSupport, IsManagement
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class ContractViewSet(viewsets.ModelViewSet):
    """A viewset that provides CRUD operations for contract."""
    serializer_class = ContractSerializer

    def get_queryset(self):
        queryset = Contract.objects.all()
        customer_id = self.kwargs.get('customer_id')
        if customer_id:
            queryset = queryset.filter(customer=customer_id)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        contract_id = self.kwargs.get('pk')
        if contract_id:
            obj = get_object_or_404(queryset, id=contract_id)
            return obj

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSale | IsManagement | IsSupport]
        elif self.action in ['update', 'partial_update']:
            if self.get_object().sales_contact == self.request.user:
                permission_classes = [IsManagement | IsSale]
            else:
                permission_classes = [IsManagement]
        elif self.action == 'create':
            permission_classes = [IsManagement | IsSale]
        elif self.action == 'destroy':
            permission_classes = [IsManagement]
        else:
            raise ValueError("Vous n'avez pas les droits")
        return [permission() for permission in permission_classes]