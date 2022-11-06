
# FORMULÁRIO PARA CADASTRAR AS TAREFAS
# ESTE FORMULÁRIO IRÁ PEGAS OS DADOS DA NOSSA MODEL  , DENTRO DELA DELA A TASK

#from django.forms import ModelForm
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'describe', 'important'] # estes dados são da models , dentro da Task

        #estilizando o fomulário do Template task_detalhe.html
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'describe': forms.Textarea(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input '}),
        }
