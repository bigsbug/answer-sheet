from django.urls import path
from .views import Home,List_quiz,Quiz,Save_quiz_answer,Result_quiz,Correct_Answers


urlpatterns = [
    path('',Home,name='HOME'),
    path('list_quiz/<str:pk>',List_quiz,name='LIST_QUIZ'),
    path('quiz/<str:pk>',Quiz,name='QUIZ'),
    path('corrent_asnwer/<str:pk>',Correct_Answers,name='ANSWER'),
    path('save_answer',Save_quiz_answer,name='SAVE_QUIZ_ANSWER'),
    path('result/<str:pk>',Result_quiz,name='RESULT_QUIZ')
]