from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers.quiz_serializer import QuizSerializer
from quiz.models import Quiz


class AdminQuizFilter(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Quiz.objects.filter((Q(name__contains=self.kwargs['value']) | Q(description__contains=self.kwargs['value'])), user=self.request.user)
