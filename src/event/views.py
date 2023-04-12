from event.models import Event
from event.serializers import EventSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    """Endpoint Api for user management(CRUD)"""

    serializer_class = EventSerializer
    queryset = Event.objects.all()