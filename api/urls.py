from django.urls import path

from api import views
from api.view_classes.admin_last_n import AdminQuizLast
from api.view_classes.admin_search import AdminQuizFilter
from api.view_classes.home_last_n import HomeQuizLast
from api.view_classes.home_search import HomeQuizFilter
from api.view_classes.liker import LikerView
from api.view_classes.messages_view import MessagesView, MessagesViewId
from api.view_classes.profile import ProfileView
from api.view_classes.classes import ClassView
from api.view_classes.teacher import TeacherView

urlpatterns = [
    path('quiz/', views.quiz),
    path('quiz/<int:id_quiz>', views.quiz),
    path('quiz/<int:cursor>/<int:amount>', views.quiz),
    path('quiz/find/<value>', HomeQuizFilter.as_view()),
    path('quiz/find/mine/<value>', AdminQuizFilter.as_view()),
    path('quiz/last/', HomeQuizLast.as_view()),

    path('profile/', ProfileView.as_view()),

    path('licence/', ProfileView.as_view()),

    path('liker/<int:id>', LikerView.as_view()),

    path('result/', views.result),
    path('result/<id_result>', views.result),

    path('allresult/<id_quiz>', views.all_result),
    path('alladminresult/', views.all_admin_result),

    path('fullquiz/', views.fullquiz),
    path('fullquiz/<int:id_quiz>', views.fullquiz),

    path('quiz/admin/', AdminQuizLast.as_view()),
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

    path('messages/', MessagesView.as_view()),
    path('message/<int:pk>', MessagesViewId.as_view()),

    path('classes/', ClassView.as_view()),

    path('teacher/', TeacherView.as_view()),

]