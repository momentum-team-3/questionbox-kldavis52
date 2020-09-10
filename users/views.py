from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserCreationForm, ChangeUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect(to='snippets')
    else:
        form = NewUserCreationForm()
        if form.is_valid():
            form.save()
            return redirect(to='snippets')

    return render(request, 'register.html', {'form': form, 'message': messages})

def login_user(request):
    retry = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to='userprofile', pk=user.pk)
        else:
            retry = True
    return render(request, 'login_user.html', {'retry': retry})

def logout_user(request):
    logout(request)
    return render(request, 'logout_user.html')

def userprofile(request):
    pass