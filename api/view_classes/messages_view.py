from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers.message.message_get import MessageGetSerializer
from api.serializers.message.message_post import MessagePostSerializer
from api.serializers.method_serializer_view import MethodSerializerView
from quiz.models import Message


class MessagesView(MethodSerializerView, generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    method_serializer_classes = {
        ('GET', ): MessageGetSerializer,
        ('POST', ): MessagePostSerializer
    }

    def get_queryset(self):
        return Message.objects.filter(Q(user_from=self.request.user) | Q(user_to=self.request.user))


class MessagesViewId(MethodSerializerView, generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    method_serializer_classes = {
        ('GET', 'DELETE'): MessageGetSerializer,
    }

    def get_queryset(self):
        return Message.objects.filter(Q(user_from=self.request.user) | Q(user_to=self.request.user))

