from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
# classe para formulários
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 1 serve para criar user o outro para logar
from django.contrib.auth.models import User
# para verificar se o user está com a senha correta
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# importando o meu arquivo form.py
from .forms import TaskForm
# importando o Task base de dados lá do models.py
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Home do Projeto.
def home(request):
    return render(request,'home.html')

#Cadastar uma pessoa
def sigup(request):

    if request.method == 'GET':

        return render(request,'sigup.html', {
            'form' : UserCreationForm
        } )   

    else: 
        if request.POST['password1'] == request.POST['password2']:

            try: 
                #registe_user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # para verificar se o user está com a senha correta
                login(request, user)
                # redirecionando para o template tasks.html
                return redirect('tasks')
                
            except:
                return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'Usuário já existe'
                    
                    } ) 
           
        return render (request,'sigup.html', { 
                    'form' : UserCreationForm ,
                    "error": 'senhas são diferentes'
                    
                    } ) 
@login_required
# Exibir as Tarefas  
def tasks(request):
    # tasks = Task.objects.all()  neste exemplo pegas as tarefas de todos os usuários
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) # pega a tarefa do usuário logado
    return render(request, 'tasks.html', { 'tasks' : tasks })


# Para sair
@login_required
def sair(request):
    logout (request)  # OBS: logout , importei lá no inicio
    return redirect('home')

#Quando a pessoa já tem conta ela loga
def sigin(request):
    if request.method == 'GET':
        return render(request, 'sigin.html', {
        'form' : AuthenticationForm
        })

    else:    
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'sigin.html', {
                 'form' : AuthenticationForm,
                 'error' : 'Usuário ou Senha incorretos'
            })

        else: 
            login(request, user)
            return redirect('tasks')    


 # Criando as Tarefas
@login_required
def criando_tarefa(request):

    if request.method == 'GET':
            return render(request,'criando_tarefa.html', {
            'form' : TaskForm

       }) 

    else:

        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')

        except ValueError:

             return render(request,'criando_tarefa.html', {
            'form' : TaskForm,
            'error': 'Favor inserir dados validos'  
             })
        
           
 # Detalhes tarefas
@login_required
def task_detalhe(request, task_id): 

    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)  # tenho que importar o get_object_or_404 serve para so ids das tarefas
        form = TaskForm(instance=task)
        return render(request,'task_detalhe.html', {'task': task, 'form': form}) 

    else:  
        try: 
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')

        except ValueError:
            return render(request,'task_detalhe.html', {'task': task, 'form': form,
            'error': "Erro ao atualizar a tarefa"}) 



 # Completar tarefas
@login_required
def complete_tarefa(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')



 # Deletar tarefas
@login_required
def deletar_tarefa(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


 # Exibir as Tarefas marcadas com COMPLETA
@login_required
def exibir_tarefas_completadas(request):
    # tasks = Task.objects.all()  neste exemplo pegas as tarefas de todos os usuários
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by # pega a tarefa do usuário logado
    ('-datecompleted') # Ordenar a exibição das Tarefas
    return render(request, 'tasks.html', { 'tasks' : tasks })