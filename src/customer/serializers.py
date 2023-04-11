from customer.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
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
