from django.shortcuts import redirect, render
from django.db.models import Count, Min
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# from django.core import serializers
from django.forms import model_to_dict

from .models import Question, Tag, Answer
from .forms import QuestionForm, AnswerForm
from users.models import User

# Create your views here.


def questions_list(request):
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    questions = Question.objects.all()
    return render(
        request,
        "qanda/questions_list.html",
        {"logged_in": logged_in, "questions": questions},
    )


@login_required
def add_question(request):
    form = QuestionForm(data=request.POST)
    if form.is_valid():
        question = form.save(commit=False)
        question.user = request.user
        question.save()
        question.set_tag_names(form.cleaned_data["tag_names"])
        return redirect(to="question_detail", pk=question.pk)
    form = QuestionForm()

    return render(request, "qanda/add_question.html", {"form": form})


@login_required
def delete_question(request, pk):
    question = Question.objects.get(pk=pk)
    question.delete()
    user = User.objects.get(pk=request.user.pk)
    questions = Question.objects.all()
    return render(
        request, "users/userprofile.html", {"user": user, "questions": questions}
    )


def question_detail(request, pk):
    if request.is_ajax and request.method == "POST":
        return redirect("add_answer")
    form = AnswerForm()
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(questions=question)
    return render(
        request,
        "qanda/question_detail.html",
        {"question": question, "answers": answers, "form": form},
    )


@csrf_exempt
@login_required
def add_answer(request, pk):
    # request should be ajax and method should be POST
    form = AnswerForm(data=request.POST)
    if form.is_valid():
        print(form)
        answer = form.save(commit=False)
        answer.user = request.user
        # answer.body =
        answer.save()
        return JsonResponse(data={"answer": model_to_dict(answer)}, status=200)
    # from error occured
    return JsonResponse(data={"error": form.errors}, status=400)
