from rest_framework import serializers
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for the user.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")

        return CustomUser.objects.create_user(email=validated_data['email'],
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'],
                                              role=validated_data['role'],
                                              password=validated_data['password'])

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
