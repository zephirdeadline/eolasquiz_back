from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers.class_serializer.class_get_serializer import ClassGetSerializer
from api.serializers.class_serializer.class_post_serializer import ClassPostSerializer
from api.serializers.method_serializer_view import MethodSerializerView
from quiz.models import Class


class ClassView(MethodSerializerView, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    method_serializer_classes = {
        ('GET', ): ClassGetSerializer,
        ('POST', ): ClassPostSerializer
    }

    def get_queryset(self):
        return Class.objects.filter(Q(school__manager=self.request.user.created_by) | Q(created_by=self.request.user))

    def perform_create(self, serializer):
        data =