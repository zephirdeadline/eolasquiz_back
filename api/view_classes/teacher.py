from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import User


class TeacherView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            data = {
                'licence_type': 'teacher',
                'email': request.data['email'],
                'licence': '',
                'created_by': request.user,
            }
            user = User(**data)
            user.set_password('AFbp12Mpl56!')
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
