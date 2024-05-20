from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Nous n'affichons pas le mot de passe lors de la sérialisation

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']  # Les champs à inclure dans la sérialisation
        extra_kwargs = {
           'password': {'write_only': True},  # Indique que le champ password ne doit pas être inclus dans les réponses
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user