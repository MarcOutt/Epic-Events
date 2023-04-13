from customer.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for the customer"""
    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_update', 'sales_contact')

    def create(self, validated_data):
        return Customer.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name'],
                                       phone=validated_data['phone'],
                                       mobile=validated_data['mobile'],
                                       company_name=validated_data['company_name'],
                                       sales_contact=validated_data['sales_contact']
                                       )

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.sales_contact = validated_data.get('sales_contact', instance.sales_contact)
        instance.save()
        return instance


