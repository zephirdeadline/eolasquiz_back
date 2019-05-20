from rest_framework import serializers

from quiz.models import Class


class ClassGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = '__all__'
