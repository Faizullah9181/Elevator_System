from rest_framework import serializers
from .models import ElevatorManager
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorManager
        fields = ['id', 'name', 'email', 'is_admin']

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ElevatorManager
        fields = ['id', 'name', 'email', 'is_admin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)