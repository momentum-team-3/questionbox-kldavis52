from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.questions_list, name='questions_list'),
    # path('search/', views., name='')
]