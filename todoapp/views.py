from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .form import New_Task


def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

@login_required
def add_todo(request):
    form = New_Task()
    if request.method == 'POST':
        form = New_Task(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.user = request.user
            task.save()
            return redirect('home')
    return render(request, 'add_todo.html', {'form': form})


@login_required
def edit_todo(request, id):
    task = get_object_or_404(Task, id=id)
    form = New_Task(instance=task)
    if request.method == 'POST':
        form = New_Task(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = New_Task(instance=task)
    return render(request, 'edit_todo.html', {'form': form, 'task': task})


@login_required
def delete_todo(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'delete_todo.html', {'task': task})