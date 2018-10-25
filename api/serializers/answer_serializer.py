from rest_framework import serializers

from quiz.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), write_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct', 'question')

    def create(self, validated_data, user=None):
        answer = Answer.objects.create(**validated_data)
        answer.save()
        return answer

    def update(self, instance, validated_data, user=None):
        answer = Answer(id=instance.id, **validated_data)
        answer.save()
        return answer
