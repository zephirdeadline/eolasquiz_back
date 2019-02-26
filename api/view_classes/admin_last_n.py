from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers.quiz_serializer import QuizSerializer
from api.standard_results_set_pagination import StandardResultsSetPagination
from quiz.models import Quiz


class AdminQuizLast(generics.ListAPIView):
    serializer_class = QuizSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user).order_by('-created_at')
