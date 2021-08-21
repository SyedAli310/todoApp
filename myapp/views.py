from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from myapp.models import TODO

import datetime
from datetime import date
import calendar


def home(request):
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()] 

    todoCount = 'Not Logged In'
    todoPendingCount = 'Not Logged In'
    if request.user.is_authenticated:
        user = request.user
        todoAdded= TODO.objects.filter(user=user)
        todoCount = len(todoAdded)
        todoPendingCount = len(TODO.objects.filter(user=user, status='Pending'))

    return render(request, 'index.html', {'day':day , 'todoCount':todoCount , 'todoPendingCount': todoPendingCount})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    if 'order' in request.session:
        del request.session['order']
    return redirect('login')

def dashboard(request,order=None):
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()] 
    if request.user.is_authenticated:
        user = request.user
        completedCount = len(TODO.objects.filter(user=user,status='Completed'))
        pendingCount = len(TODO.objects.filter(user=user,status='Pending'))
        if order == 'newest':
            request.session['order'] = '-date'
            todos = TODO.objects.filter(user=user).order_by('-date')
            return render(request, 'dashboard.html',{'todos':todos , 'day':day , 'completedCount':completedCount, 'pendingCount':pendingCount})
        elif order == 'pending':
            request.session['order'] = '-status'
            todos = TODO.objects.filter(user=user).order_by('-status')
            return render(request, 'dashboard.html',{'todos':todos , 'day':day, 'completedCount':completedCount, 'pendingCount':pendingCount})
        elif order == 'priority':
            request.session['order'] = 'priority'
            todos = TODO.objects.filter(user=user).order_by('priority')
            return render(request, 'dashboard.html',{'todos':todos , 'day':day, 'completedCount':completedCount, 'pendingCount':pendingCount})
        else:
            if 'order' in request.session:
                todos = TODO.objects.filter(user=user).order_by(request.session['order'])
                return render(request, 'dashboard.html',{'todos':todos , 'day':day, 'completedCount':completedCount, 'pendingCount':pendingCount})
            else:
                todos = TODO.objects.filter(user=user)
                return render(request, 'dashboard.html',{'todos':todos , 'day':day, 'completedCount':completedCount, 'pendingCount':pendingCount})
    else:
        return redirect('login')

def add_todo(request):
    if request.user.is_authenticated and request.method == 'POST':
        
        user = request.user
        title = request.POST['title']
        status = request.POST['status']
        priority = request.POST['priority']
        date = datetime.datetime.now()
        
        if status == 'Select Status':
            messages.info(request, 'Please select status')
            return redirect('dashboard')  
        elif priority == 'Select Priority':
            messages.info(request, 'Please select a priority')
            return redirect('dashboard')
        else:
            todo = TODO.objects.create(title=title, status=status, priority=priority, user=user, date=date)
            todo.save();
            return redirect('dashboard')  
    else:
        return render(request,'dashboard.html')

def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('dashboard')

def change_status(request,id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('dashboard')

def searchTodo(request):
    my_date = date.today()
    day = calendar.day_name[my_date.weekday()] 
    if request.method=='GET' and request.user.is_authenticated:
        user = request.user
        completedCount = len(TODO.objects.filter(user=user,status='Completed'))
        pendingCount = len(TODO.objects.filter(user=user,status='Pending'))
        searchTodo = request.GET['searchTodo']
        todos = TODO.objects.filter(user=user, title__icontains=searchTodo)
        return render(request, 'dashboard.html', {'todos':todos, 'day':day, 'completedCount':completedCount, 'pendingCount':pendingCount })
    else:
        return redirect('dashboard')

def feedback(request):
    return render(request, 'feedback.html')