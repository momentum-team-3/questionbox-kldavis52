from django import forms
from django.forms import CharField, Textarea, TextInput
from .models import Question, Answer, Tag

class QuestionForm(forms.ModelForm):
    tag_names = forms.CharField(
        label="Tags",
        help_text="Enter tags separated by spaces.",
        widget=forms.TextInput(),
        required=False)
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
        ]
        widgets = {
            'title': forms.TextInput(),
            'body': forms.Textarea(),
        }
 
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'body',
        ]
        widgets = {
            'body': forms.Textarea()
        }
