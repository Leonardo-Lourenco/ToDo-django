from django.contrib import admin
from .models import Task


# Para quando for editar uma tarefa no painel ADM apareça a data de criação
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)