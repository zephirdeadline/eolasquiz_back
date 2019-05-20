from rest_framework import serializers

from quiz.models import Message


class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

