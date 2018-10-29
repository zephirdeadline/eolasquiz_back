from rest_framework import serializers

from api.serializers.dislike_serializer import DislikeSerializer
from api.serializers.full_quiz_serializer.complete_question_serializer import CompleteQuestionSerializer
from api.serializers.like_serializer import LikeSerializer
from api.serializers.question_serializer import QuestionSerializer
from quiz.models import Quiz, Question, Answer, Like, Result


class CompleteQuizSerializer(serializers.ModelSerializer):
    questions = CompleteQuestionSerializer(many=True)



    class Meta:
        model = Quiz
        exclude = ('created_at', 'user')

    def create(self, validated_data, user=None):
        questions = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data, user=user)
        quiz.save()
        for question in questions:
            answers = question.pop('answers')
            question = Question(**question)
            question.quiz = quiz
            question.save()
            for answer in answers:
                answer = Answer(**answer)
                answer.question = question
                answer.save()
        return quiz

    def update(self, instance, validated_data):
        questions = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data, user=instance.user)
        quiz.save()
        for question in questions:
            answers = question.pop('answers')
            question = Question(**question)
            question.quiz = quiz
            question.save()
            for answer in answers:
                answer = Answer(**answer)
                answer.question = question
                answer.save()

        likes = Like.objects.filter(quiz=instance)
        for like in likes:
            like.quiz = quiz
            like.save()

        dislikes = Like.objects.filter(quiz=instance)
        for dislike in dislikes:
            dislike.quiz = quiz
            dislike.save()

        results = Result.objects.filter(quiz=instance)
        for result in results:
            result.quiz = quiz
            result.save()

        instance.delete()

        return quiz