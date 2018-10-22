from rest_framework import serializers

from api.serializers.question_serializer import QuestionSerializer
from quiz.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('name', 'questions',)

    def create(self, validated_data, user=None):
        quiz = Quiz.objects.create(**validated_data, user=user)
        quiz.save()
        return quiz

    def update(self, instance, validated_data, user=None):
        quiz = Quiz(id=instance.id, **validated_data, user=instance.user)
        quiz.save()
        return quiz
