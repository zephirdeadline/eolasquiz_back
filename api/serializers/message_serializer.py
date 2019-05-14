from rest_framework import serializers

from api.serializers.user_serializer import UserSerializer
from quiz.models import Result, Quiz, User, Message


class MessageSerializer(serializers.ModelSerializer):
    user_to = UserSerializer
    user_from = UserSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'create':
            return serializers.PrimaryKeyRelatedField
        return UserSerializer

    class Meta:
        model = Message
        # fields = '__all__'
        fields = '__all__'

