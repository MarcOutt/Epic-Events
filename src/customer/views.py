from crm.permissions import IsSale, IsManagement, IsSupport
from customer.models import Customer
from customer.serializers import CustomerSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """A viewset that provides CRUD operations for customer."""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        customer_id = self.kwargs.get('pk')
        if customer_id:
            obj = get_object_or_404(queryset, id=customer_id)
            return obj

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsSale | IsManagement | IsSupport]
        elif self.action in ['update', 'partial_update']:
            if self.get_object().sales_contact == self.request.user:
                permission_classes = [IsSale | IsManagement]
            else:
                permission_classes = [IsManagement]
        elif self.action == 'create':
            permission_classes = [IsManagement | IsSale]
        elif self.action == 'destroy':
            permission_classes = [IsManagement]
        else:
            raise ValueError("Vous n'avez pas les droits")
        return [permission() for permission in permission_classes]
