from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.questions_list, name='questions_list'),
    path('add/', views.add_question, name='add_question'),
    path('<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('<int:pk>/question_detail/', views.question_detail, name='question_detail'),
    # path('search/', views., name='')
]