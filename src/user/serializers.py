from rest_framework import serializers
from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer pour la classe User.
    Convertit les objets User en données JSON et vice versa.
    Attributes:
        id (int): The user's ID.
        first_name (str): Le prénom de l'utilisateur.
        last_name (str): Le nom de famille de l'utilisateur.
        email (str): The user's email.
        password (str): Le mot de passe de l'utilisateur. Cet attribut est write-only.
    """

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Crée un nouvel utilisateur en utilisant les données validées fournies.
        Args:
            validated_data (dict): Données validées pour la création d'un nouvel utilisateur.
        Returns:
            CustomUser: L'utilisateur créé.
        """
        email = validated_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")

        return CustomUser.objects.create_user(email=validated_data['email'],
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'],
                                              user_type=validated_data['role'],
                                              password=validated_data['password'])