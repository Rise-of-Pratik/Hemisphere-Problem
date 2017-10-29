from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password', 'phone', 'picture')