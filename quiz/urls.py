from quiz.views import result
from django.urls import path

from . import views



app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('chap<num>/', views.quiz_for_chapteri, name="chap_quiz"),
    path('result/', views.result, name='result'),
    path('addQues/', views.add_question,name='add_Quesiton'),
    path('addOpt/<int:ques_id>', views.add_Option, name='add_Option')
]