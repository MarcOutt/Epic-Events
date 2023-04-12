from crm.permissions import IsManagement, IsSale, IsSupport
from event.models import Event
from event.serializers import EventSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""
    permission_classes = [IsManagement]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsSale, IsSupport]
        elif self.action == 'create':
            permission_classes = [IsSale]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsSupport]
        return [permission() for permission in permission_classes]