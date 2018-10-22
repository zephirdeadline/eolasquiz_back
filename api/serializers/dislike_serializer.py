from django.contrib.auth.models import User
from rest_framework import serializers

from quiz.models import Quiz, Dislike, Like


class DislikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all(), write_only=True)

    class Meta:
        model = Dislike
        fields = ('quiz', 'user')

    def create(self, validated_data, user=None):
        dislike = Dislike.objects.create(**validated_data, user=user)
        try:
            Like.objects.get(user=user, quiz=dislike.quiz).delete()
        except:
            pass
        dislike.save()
        return dislike

