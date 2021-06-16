from django import forms
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"
        widgets = {
            'due_time': DateInput(),
        }


