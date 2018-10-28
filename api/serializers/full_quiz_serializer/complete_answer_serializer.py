from rest_framework import serializers

from quiz.models import Answer, Question


class CompleteAnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data, user=None):
        answer = Answer.objects.create(**validated_data)
        answer.save()
        return answer

    def update(self, instance, validated_data, user=None):
        answer = Answer(id=instance.id, **validated_data)
        answer.save()
        return answer