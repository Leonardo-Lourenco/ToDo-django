from django.shortcuts import render, redirect
# classe para formulários
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# para verificar se o user está com a senha correta
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request,'home.html')

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

    
def tasks(request):
    return render(request,'tasks.html')



