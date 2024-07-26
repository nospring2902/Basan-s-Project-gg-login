from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .form import TaskForm, UserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateformat import format
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

# Create your views here.

def main(request):
    if request.method=='POST':
        return redirect('create-tasks')
    
    return render(request, 'index.html')

def temp(request):
    return render(request, 'index.html')

def homepage(request):
    
    return render(request, 'homepage.html')

@login_required(login_url='log_in')  
def CreateForm(request):

    form= TaskForm()
    
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task= form.save(commit=False)
            
            task.user=request.user
            task.save()
            return redirect('dashboard')
    
    
    context={'formm': form}
    return render(request, 'profile/CreateForm.html', context=context)

@login_required(login_url='log_in')
def UpdateForm(request, pk):
    
    task=Task.objects.get(id=pk)
    
    if request.method=='POST':
        
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-tasks')
        
    else:
        form=TaskForm(instance=task)
        
    context={'formm': form}
    return render(request, 'profile/update.html', context=context)


@login_required(login_url='log_in')
def DeleteForm(request, pk):
    
    task=Task.objects.get(id=pk)
    
    if request.method=='POST':
        
        task.delete()
        return redirect('view-tasks')
        
    context={'formm': task}
    return render(request, 'profile/delete.html', context=context)


def register(request):
    
    form=UserForm()
    
    if request.method=='POST':
        
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
        
    context={'formm': form}
    return render(request, 'register.html', context=context)

def log_in(request):
    
    form=LoginForm()
    
    if request.method=='POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return render(request, 'profile/dashboard.html')
            
    context={'form': form}
    return render(request, 'login.html', context=context)

@login_required(login_url='log_in')
def dashboard(request):
    tasks = Task.objects.all().filter(user=request.user)
    tasks_data = []
    for task in tasks:
        tasks_data.append({
            'title': task.title,
            'deadline': format(task.deadline, 'c'),  # ISO 8601 format
        })
    return render(request, 'profile/dashboard.html', {'tasks': tasks_data})

@login_required(login_url='log_in')
def viewtasks(request):
    current_user=request.user.id
    
    task=Task.objects.all().filter(user=current_user)
    
    context={'task': task}
    return render(request, 'profile/view-tasks.html', context=context)

@login_required(login_url='log_in') 
def log_out(request):
    auth.logout(request)
    return redirect('homepage')

def basan(request):
    
    if request.method=='POST':
        return render(request, 'logindemo.html')
    
    return render(request, 'logindemo.html')

                
    
    
    
    
    
        
        
            
    
            
    
    
    
        
    