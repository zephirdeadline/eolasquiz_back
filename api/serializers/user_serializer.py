from rest_framework import serializers

from quiz.models import Result, Quiz, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'licence_type')

