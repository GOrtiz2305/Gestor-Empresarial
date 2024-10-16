from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def homepage(request):
    return render(request, 'principal/homepage.html')

def signin(request):
    if request.method=='GET':
        return render(request,'principal/signin.html')
    else:
        user = authenticate(request,username = request.POST['user'],password = request.POST['password'])
        if user is None:
            return render(request,'principal/signin.html',{
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
           login(request,user)
           return redirect ('/')
        
def signout(request):
    logout(request)
    return redirect ('/')