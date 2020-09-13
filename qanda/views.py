from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import AnonymousUser
from django.db.models import Count, Min
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import Question, Tag, Answer
from users.models import User
from .forms import QuestionForm, AnswerForm

# Create your views here.

def questions_list(request):
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    questions = Question.objects.all()
    return render(request, 'qanda/questions_list.html', {'logged_in': logged_in, 'questions': questions})

@login_required
def add_question(request):
    form = QuestionForm(data=request.POST)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        question.set_tag_names(form.cleaned_data['tag_names'])
        return redirect(to='question_detail', pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, 'qanda/add_question.html', {'form': form})

@login_required
def delete_question(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    user = User.objects.get(pk=request.user.pk)
    questions = Question.objects.all()
    return render(request, 'users/userprofile.html', {'user': user, 'questions': questions})

def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.save()
            return redirect(to='add_answer', pk=question.pk)
    else:
        form = AnswerForm()
    
    answers = Answer.objects.filter(questions=question)
    return render(request, 'qanda/question_detail.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def add_answer(request, pk):
    return redirect('question_detail', pk=pk)
