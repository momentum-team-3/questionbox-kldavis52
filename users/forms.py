from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import User

class NewUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class ChangeUserForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields