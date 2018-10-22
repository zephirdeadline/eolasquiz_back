from rest_framework import serializers

from api.serializers.answer_serializer import AnswerSerializer

from quiz.models import Answer, Question, Quiz


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all(), write_only=True)

    class Meta:
        model = Question
        fields = ('text', "quiz", 'answers')

    def create(self, validated_data, user=None):
        question = Question.objects.create(**validated_data)
        question.save()
        return question

    def update(self, instance, validated_data, user=None):
        question = Question(id=instance.id, **validated_data)
        question.save()
        return question
