from http.client import ImproperConnectionState
from django.shortcuts import render, redirect
# classe para formulários
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 1 serve para criar user o outro para logar
from django.contrib.auth.models import User
from django.http import HttpResponse
# para verificar se o user está com a senha correta
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# importando o meu arquivo form.py
from .forms import TaskForm
# importando o Task base de dados lá do models.py
from .models import Task



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

# Exibir as Tarefas  
def tasks(request):
    # tasks = Task.objects.all()  neste exemplo pegas as tarefas de todos os usuários
    tasks = Task.objects.filter(user=request.user) # pega a tarefa do usuário logado
    return render(request, 'tasks.html', { 'tasks' : tasks })

# Para sair
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
        
           
          
    
