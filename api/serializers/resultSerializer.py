from rest_framework import serializers

from quiz.models import Result, Quiz


class ResultSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())

    class Meta:
        model = Result
        fields = '__all__'

    def create(self, validated_data, user=None):
        result = Result(**validated_data)
        result.save()
        return result

