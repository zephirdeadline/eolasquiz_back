from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.class_serializer.class_get_serializer import ClassGetSerializer
from api.serializers.class_serializer.class_post_serializer import ClassPostSerializer
from api.serializers.method_serializer_view import MethodSerializerView
from quiz.models import Class, School


class ClassView(MethodSerializerView, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    method_serializer_classes = {
        ('GET', ): ClassGetSerializer,
        ('POST', ): ClassPostSerializer
    }

    def get_queryset(self):
        return Class.objects.filter(Q(school__manager=self.request.user.created_by) | Q(created_by=self.request.user))

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.licence_type == 'teacher':
            school = School.objects.get(manager=user.created_by)
        else:
            school = School.objects.get(manager=user)
        data = {
            'name': self.request.data["name"],
            'created_by': user.id,
            'school': school.id
        }
        serial = ClassPostSerializer(data=data)
        if serial.is_valid():
            serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)