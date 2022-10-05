from django.db import models

from django.contrib.auth.models import User # OBS: Importau a tabela usuário que já vem quando instalamos o DJango,
#vamos usar ela na model/ tabela abaixo para relacionar a Tarefa ao usuário LogadO

# Create your models here.
#  Model para guardar as Tarefas
class Task(models.Model):
    title = models.CharField(max_length=100)
    describe = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)