from django import forms
from .models import Task

class New_Task(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['text', 'is_done']
