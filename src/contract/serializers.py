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

    def update(self, instance, validated_data):
        instance.sales_contact = validated_data.get('sales_contact', instance.sales_contact)
        instance.status = validated_data.get('status', instance.status)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.payment_due = validated_data.get('payment_due', instance.payment_due)
        instance.save()

        return instance
