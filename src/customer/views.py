from crm.permissions import IsSale, IsManagement, IsSupport
from customer.models import Customer
from customer.serializers import CustomerSerializer
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""
    permission_classes = [IsManagement]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsSale, IsSupport]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsSale]
        return [permission() for permission in permission_classes]
