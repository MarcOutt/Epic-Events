
from contract.models import Contract
from contract.serializers import ContractSerializer
from crm.permissions import IsSale, IsSupport, IsManagement
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from event.models import Event
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

    @receiver(post_save, sender=Contract)
    def create_event(sender, instance, **kwargs):
        # sourcery skip: instance-method-first-arg-name
        try:
            event = Event.objects.get(contract=instance)
        except Event.DoesNotExist:
            Event.objects.create(
                customer=instance.customer,
                contract=instance,
                event_ended=False,
                attendees=0,
                notes='',
            )