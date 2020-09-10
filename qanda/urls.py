from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('questions/', views.questions, name='questions'),
    # path('search/', views., name='')
]