from http.client import HTTPResponse
import imp
from django.shortcuts import render
# classe para formulários
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def sigup(request):

    if request.method == 'GET':

        return render(request,'sigup.html', {
            'form' : UserCreationForm
        } )   

    else: 
        if request.POST['password1'] == request.POST['password1']:
            #registe_user
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save()
            return HTTPResponse('User created successful')
        return HttpResponse('Password do not match')    

    


