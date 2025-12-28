from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)  
        if form.is_valid(): # calls authenticate() internally 
            user = form.get_user()  
            login(request, user)
            UserRole = Profile.objects.get(user = user)
            if UserRole.role == 'admin':
                return redirect('AdminDashboard')
            elif UserRole.role == 'user':
                return redirect('UserDashboard')
        else: 
            return render(request, 'accounts/login.html', {'form' : form}) 
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form' : form}) 

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user = user)
            return redirect('login') 
        else:
            for field in form.fields.values():
                field.widget.attrs['class'] = 'form-control'
            return render(request, 'accounts/register.html', {'form':form})

    form = RegisterForm()
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'

    return render(request, 'accounts/register.html', {'form':form})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')