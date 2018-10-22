from django.contrib.auth.models import User
from rest_framework import serializers

from quiz.models import Quiz, Dislike, Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all(), write_only=True)

    class Meta:
        model = Like
        fields = ('user', 'quiz')

    def create(self, validated_data, user=None):
        like = Like.objects.create(**validated_data, user=user)
        try:
            Dislike.objects.get(user=user, quiz=like.quiz).delete()
        except:
            pass
        like.save()
        return like

