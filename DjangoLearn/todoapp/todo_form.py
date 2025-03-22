from django import forms
from .models import Todos

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description', 'importance', 'done_upto']
        widgets = {
            'done_upto': forms.DateInput(attrs={'type': 'date'}),
        }