from django.urls import path
from . import views


urlpatterns = [
    path("", views.questions_list, name="questions_list"),
    path("add/", views.add_question, name="add_question"),
    path("<int:pk>/delete/", views.delete_question, name="delete_question"),
    path("<int:pk>/question_detail/", views.question_detail, name="question_detail"),
    path("<int:pk>/add_answer/", views.add_answer, name="add_answer"),
    # path('search/', views., name='')
]
