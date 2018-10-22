from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=64)
    difficulty = models.IntegerField()
    is_moderated = models.BooleanField(default=False)
    name = models.CharField(max_length=64)


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=256)


class Answer(models.Model):
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'quiz')


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='dislikes')

    class Meta:
        unique_together = ('user', 'quiz')