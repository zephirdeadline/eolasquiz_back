from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.dislike_serializer import DislikeSerializer
from api.serializers.like_serializer import LikeSerializer
from quiz.models import Quiz


class LikerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        quiz = Quiz.objects.get(id=id)
        likes = LikeSerializer(quiz.likes, many=True).data
        dislikes = DislikeSerializer(quiz.dislikes, many=True).data
        return Response({'likes': likes, 'dislikes': dislikes})
