from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    status = False
    if User.objects.filter(username='admin'):
        status = True
        print('admin')
    else :
        admin = User.objects.create_superuser(username='admin', password='admin', email='admin001@gmail.com')
        if admin:
            print('create admin')
            status = True
        else :
            status = False
        
    
    
    return  redirect('homepage')

def homepage(request):
    
    return render(request, 'homepage.html')

