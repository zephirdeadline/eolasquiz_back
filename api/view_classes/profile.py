
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user_serializer import UserSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = UserSerializer(instance=request.user, data=request.data)
        if user.is_valid():
            user.save()
        return Response(user.data)

    def get(self, request):
        user = UserSerializer(instance=request.user)
        return Response(user.data)
