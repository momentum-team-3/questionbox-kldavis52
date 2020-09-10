from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import AnonymousUser

# Create your views here.

def homepage(request):
    if not isinstance(request.user, AnonymousUser):
        return redirect(to='questions')
    return render(request, 'qanda/homepage.html')

def questions(request):
    return render(request, 'qanda/questions.html')