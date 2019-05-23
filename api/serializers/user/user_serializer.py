from rest_framework import serializers

from quiz.models import Result, Quiz, User, School


class UserSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'licence_type', 'school')

    def get_school(self, user):
        if user.licence_type == 'teacher':
            return School.objects.get(manager=user.created_by).name
        elif user.licence_type == 'school':
            return School.objects.get(manager=user).name
        if user.licence_type == 'student':
            return School.objects.get(manager=user.created_by.created_by).name
        else:
            return None
