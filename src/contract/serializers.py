from contract.models import Contract
from rest_framework import serializers


class ContractSerializer(serializers.ModelSerializer):
    """Serializer for the contract"""
    class Meta:
        model = Contract
        fields = ('id', 'sales_contact', 'status', 'amount', 'payment_due')

    def create(self, validated_data):
        customer_id = self.context['view'].kwargs['customer_id']
        validated_data['customer_id'] = customer_id

        if not validated_data['status']:
            raise serializers.ValidationError("Le contrat ne peut pas être créé car le status n'est pas validé.")

        return Contract.objects.create(**validated_data)

