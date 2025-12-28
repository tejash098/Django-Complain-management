from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import login, logout
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid(): # calls authenticate() internally 
            user = form.get_user()
            login(request, form.user)
            return HttpResponse('Logged in') #! to be modify
        else: 
            return render(request, 'accounts/login.html', {'form' : form}) 
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form' : form}) 

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view') 
        else:
            for field in form.fields.values():
                field.widget.attrs['class'] = 'form-control'
            return render(request, 'accounts/register.html', {'form':form})

    form = RegisterForm()
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'

    return render(request, 'accounts/register.html', {'form':form})