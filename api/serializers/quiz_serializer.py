from rest_framework import serializers

from api.serializers.dislike_serializer import DislikeSerializer
from api.serializers.like_serializer import LikeSerializer
from api.serializers.question_serializer import QuestionSerializer
from quiz.models import Quiz, User


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    dislikes = DislikeSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    is_cert_teacher = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'name', 'questions', 'likes', 'dislikes', 'description', 'created_at', 'category', 'difficulty', 'is_cert_teacher')

    def create(self, validated_data, user=None):
        quiz = Quiz.objects.create(**validated_data, user=user)
        quiz.save()
        return quiz

    def update(self, instance, validated_data, user=None):
        quiz = Quiz(id=instance.id, **validated_data, user=instance.user)
        quiz.save()
        return quiz

    def get_is_cert_teacher(self, quiz):
        try:
            return quiz.user.licence_type == 'teacher'
        except:
            return False
