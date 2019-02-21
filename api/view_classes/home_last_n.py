from django.db.models import Q
from rest_framework import generics

from api.serializers.quiz_serializer import QuizSerializer
from api.standard_results_set_pagination import StandardResultsSetPagination
from quiz.models import Quiz


class HomeQuizLast(generics.ListAPIView):
    serializer_class = QuizSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Quiz.objects.order_by('created_at')
