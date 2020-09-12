from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.questions_list, name='questions_list'),
    path('add/', views.add_question, name='add_question'),
    path('question_detail/<int:pk>/', views.question_detail, name='question_detail')
    # path('search/', views., name='')
]