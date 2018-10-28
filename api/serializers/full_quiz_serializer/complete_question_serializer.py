from rest_framework import serializers

from api.serializers.full_quiz_serializer.complete_answer_serializer import CompleteAnswerSerializer
from quiz.models import Question, Quiz, Answer


class CompleteQuestionSerializer(serializers.ModelSerializer):
    answers = CompleteAnswerSerializer(many=True, )
    quiz = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data, user=None):
        answers = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)

        question.answers.set([Answer(**item) for item in answers])
        question.save()
        return question

    def update(self, instance, validated_data, user=None):
        question = Question(id=instance.id, **validated_data)
        question.save()
        return question