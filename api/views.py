import uuid

from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_object.view import action

from api.serializers.answer_serializer import AnswerSerializer
from api.serializers.dislike_serializer import DislikeSerializer
from api.serializers.full_quiz_serializer.complete_quiz_serializer import CompleteQuizSerializer
from api.serializers.like_serializer import LikeSerializer
from api.serializers.question_serializer import QuestionSerializer
from api.serializers.quiz_serializer import QuizSerializer
from api.serializers.resultSerializer import ResultSerializer
from quiz.models import Quiz, Like, Dislike, Question, Answer, Result, Class, User, Message, School


def question(request, cursor=None, amount=None, id_question=None):
    return action(request, Question, QuestionSerializer, id_question, cursor=cursor, amount=amount, is_restricted=True, linked_to_user=False)


@api_view(['GET'])
def all_result(request, id_quiz):
    return Response(ResultSerializer(Result.objects.filter(quiz_id=id_quiz), many=True).data)


@api_view(['GET'])
def all_admin_result(request):
    return Response(ResultSerializer(Result.objects.filter(quiz__user=request.user).order_by('-date_done')[:10], many=True).data)


@api_view(['GET'])
def get_result(request, id_result):
    try:
        result = Result.objects.get(uniq_id=id_result)
        return Response(ResultSerializer(result).data)
    except Exception as e:
        return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_my_result(request):
    result = Result.objects.filter(user=request.user)
    return Response(ResultSerializer(result, many=True).data)


@api_view(['POST'])
def post_result(request):
    data = request.data[0]
    if type(request.user) != AnonymousUser:
        data['user'] = request.user.id
    res = ResultSerializer(data=data)
    if res.is_valid():
        res.save()
        return Response(res.data, status=status.HTTP_201_CREATED)
    else:
        return Response(res.errors, status=status.HTTP_400_BAD_REQUEST)



def result(request, cursor=None, amount=None, id_result=None):
    if request.method == 'GET':
        return get_result(request, id_result)
    else:
        return post_result(request)


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


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def broadcast_quiz(request):
    classe = Class.objects.get(id=request.data['classe'])
    students = User.objects.filter(class_entity_id=classe, licence_type='student')
    school = School.objects.get(manager=request.user.created_by)
    for student in students:
        Message.objects.create(user_from=request.user, user_to=student, content="https://quiz.w4pity.fr/test/" + request.data['quiz'] +"/10/"+school.name+'_'+str(classe.id)+'_'+str(student.id)+'_'+str(uuid.uuid4()), subject='mission todo')
    return Response(status=status.HTTP_201_CREATED)
