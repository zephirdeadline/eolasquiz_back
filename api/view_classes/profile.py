import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user.user_serializer import UserSerializer
from quiz.models import School


def generateLicence(user):
    return 'licence:' + str(hash((user.email, user.licence_type)))


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        user = UserSerializer(instance=request.user, data=request.data)
        if user.is_valid():
            user.save()
        return Response(user.data)

    def patch(self, request):
        request.user.licence = generateLicence(request.user)
        user = UserSerializer(instance=request.user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            School.objects.create(name=uuid.uuid4(), manager=request.user)
        return Response(user.data)

    def get(self, request):
        user = UserSerializer(instance=request.user)
        return Response(user.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        user.licence = generateLicence(user)
        return Response(user.data)
