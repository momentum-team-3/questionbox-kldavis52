from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import AnonymousUser
from .models import Question, Tag, Answer
from users.models import User
# Create your views here.
    

def questions_list(request):
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    questions = Question.objects.all()
    return render(request, 'qanda/questions_list.html', {'logged_in': logged_in, 'questions': questions})