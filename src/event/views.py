from crm.permissions import IsManagement, IsSale, IsSupport
from django.shortcuts import get_object_or_404
from event.models import Event
from event.serializers import EventSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    """A viewset that provides CRUD operations for event."""
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        contract_id = self.kwargs.get('contract_id')
        if contract_id:
            queryset = queryset.filter(contract=contract_id)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        event_id = self.kwargs.get('pk')
        if event_id:
            obj = get_object_or_404(queryset, id=event_id)
            return obj

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsSale | IsManagement | IsSupport]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsManagement]
            if self.get_object().support_contact == self.request.user:
                permission_classes = [IsSupport | IsManagement]
        elif self.action == 'create':
            permission_classes = [IsManagement | IsSale]
        elif self.action == 'destroy':
            permission_classes = [IsManagement]
        else:
            raise ValueError("Vous n'avez pas les droits")
        return [permission() for permission in permission_classes]
