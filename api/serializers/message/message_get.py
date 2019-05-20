from rest_framework import serializers

from api.serializers.user.user_serializer import UserSerializer
from quiz.models import Message


class MessageGetSerializer(serializers.ModelSerializer):
    user_to = UserSerializer

    class Meta:
        model = Message
        fields = '__all__'

