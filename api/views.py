from django.shortcuts import render

# Create your views here.
from rest_object.view import action

from api.serializers.answer_serializer import AnswerSerializer
from api.serializers.dislike_serializer import DislikeSerializer
from api.serializers.full_quiz_serializer.complete_quiz_serializer import CompleteQuizSerializer
from api.serializers.like_serializer import LikeSerializer
from api.serializers.question_serializer import QuestionSerializer
from api.serializers.quiz_serializer import QuizSerializer
from quiz.models import Quiz, Like, Dislike, Question, Answer


def question(request, cursor=None, amount=None, id_question=None):
    return action(request, Question, QuestionSerializer, id_question, cursor=cursor, amount=amount, is_restricted=True, linked_to_user=False)


def answer(request, cursor=None, amount=None, id_answer=None):
    return action(request, Answer, AnswerSerializer, id_answer, cursor=cursor, amount=amount, is_restricted=True, linked_to_user=False)


def quiz(request, cursor=None, amount=None, id_quiz=None):
    if request.method == 'GET':
        return action(request, Quiz, QuizSerializer, id_quiz, cursor=cursor, amount=amount, is_restricted=False, linked_to_user=False)
    else:
        return action(request, Quiz, QuizSerializer, id_quiz, cursor=cursor, amount=amount, is_restricted=True,
                      linked_to_user=True)


def fullquiz(request, cursor=None, amount=None, id_quiz=None):

    return action(request, Quiz, CompleteQuizSerializer, id_quiz, cursor=cursor, amount=amount, is_restricted=True,
                      linked_to_user=True)


def quizadmin(request, cursor=None, amount=None, id_quiz=None):
    if request.method == 'GET':
        return action(request, Quiz, QuizSerializer, id_quiz, cursor=cursor, amount=amount, is_restricted=False, linked_to_user=True)
    else:
        return action(request, Quiz, QuizSerializer, id_quiz, cursor=cursor, amount=amount, is_restricted=True,
                      linked_to_user=True)



def like(request, cursor=None, amount=None, id_like=None):
    return action(request, Like, LikeSerializer, id_like, cursor=cursor, amount=amount, is_restricted=False, linked_to_user=True)


def dislike(request, cursor=None, amount=None, id_dislike=None):
    return action(request, Dislike, DislikeSerializer, id_dislike, cursor=cursor, amount=amount, is_restricted=False, linked_to_user=True)
