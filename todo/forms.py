from secrets import choice
from telnetlib import STATUS
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description', 'status', 'date', 'text']
        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control', 'id':'description'}),
            'status':forms.Select(attrs={'class':'form-control select-status', 'id':'text'}),
            'date':forms.TextInput(attrs={'class':'form-control due-date', 'id':'status'}),
        }
