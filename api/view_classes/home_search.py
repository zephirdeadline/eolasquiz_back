from django.db.models import Q
from rest_framework import generics

from api.serializers.quiz_serializer import QuizSerializer
from quiz.models import Quiz


class HomeQuizFilter(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        return Quiz.objects.filter(Q(name__contains=self.kwargs['value']) | Q(description__contains=self.kwargs['value']))
