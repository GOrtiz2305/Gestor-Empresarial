from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def homepage(request):
    return render(request, 'principal/homepage.html')

def signin(request):
    return render(request, 'principal/signin.html')