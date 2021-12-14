from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        labels = {
            'title': 'Titulo',
            'content': 'Contenido'
        }