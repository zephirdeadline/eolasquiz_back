from django.urls import path

from api import views
from api.view_classes.home_search import HomeQuizFilter

urlpatterns = [
    path('quiz/', views.quiz),
    path('quiz/<int:id_quiz>', views.quiz),
    path('quiz/<int:cursor>/<int:amount>', views.quiz),
    path('quiz/find/<value>', HomeQuizFilter.as_view()),

    path('result/', views.result),
    path('result/<id_result>', views.result),

    path('allresult/<id_quiz>', views.all_result),

    path('fullquiz/', views.fullquiz),
    path('fullquiz/<int:id_quiz>', views.fullquiz),

    path('quiz/admin/', views.quizadmin),
    path('quiz/admin/<int:id_quiz>', views.quizadmin),
    path('quiz/admin/<int:cursor>/<int:amount>', views.quizadmin),
    
    path('question/', views.question),
    path('question/<int:id_question>', views.question),
    path('question/<int:cursor>/<int:amount>', views.question),
    
    path('answer/', views.answer),
    path('answer/<int:id_answer>', views.answer),
    path('answer/<int:cursor>/<int:amount>', views.answer),
    
    path('like/', views.like),
    path('like/<int:id_like>', views.like),
    path('like/<int:cursor>/<int:amount>', views.like),
    
    path('dislike/', views.dislike),
    path('dislike/<int:id_dislike>', views.dislike),
    path('dislike/<int:cursor>/<int:amount>', views.dislike),

]