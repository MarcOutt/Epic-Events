from contract.models import Contract
from event.models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'support_contact', 'event_ended', 'attendees', 'event_date', 'notes')

    def create(self, validated_data):
        customer_id = self.context['view'].kwargs['customer_id']
        contract_id = self.context['view'].kwargs['contract_id']
        contract = Contract.objects.get(id=contract_id)
        if not contract.status:
            raise serializers.ValidationError("Impossible de créer un évènement car le contrat n'a pas été signé")
        validated_data['customer_id'] = customer_id
        validated_data['contract_id'] = contract_id
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if instance.event_ended:
            raise serializers.ValidationError("L'évènement est fini")
        instance.support_contact = validated_data.get('support_contact', instance.support_contact)
        instance.event_ended = validated_data.get('event_ended', instance.event_ended)
        instance.attendees = validated_data.get('attendees', instance.attendees)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
