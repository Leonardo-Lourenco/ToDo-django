
# FORMULÁRIO PARA CADASTRAR AS TAREFAS
# ESTE FORMULÁRIO IRÁ PEGAS OS DADOS DA NOSSA MODEL  , DENTRO DELA DELA A TASK

from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'describe', 'important'] # estes dados são da models , dentro da Task
