from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Message(models.Model):
    user_from = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_from")
    user_to = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_to")
    content = models.TextField()
    subject = models.CharField(max_length=200)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    licence_type = models.CharField(max_length=200, null=True)
    licence = models.CharField(max_length=200, null=True)
    expire = models.DateField(null=True)
    boss = models.ForeignKey('User', models.CASCADE, null=True)
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, max_length=200)
    REQUIRED_FIELDS = []

    objects = UserManager()


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=64)
    difficulty = models.IntegerField()
    is_moderated = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(null=True, auto_now=True)


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


class Result(models.Model):
    uniq_id = models.CharField(max_length=64, unique=True)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    score = models.FloatField()
    date_done = models.DateTimeField(auto_now=True)


