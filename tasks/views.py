from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import urls
from .models import *
from .forms import *
from .filters import *


def index(request):
  
    tasks = Task.objects.all()
    filter = taskFilter(request.GET, queryset=tasks)
    tasks = filter.qs
    form  = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = { 'tasks': tasks, 'form':form, 'filter':filter}
    return render(request, 'tasks/list.html', context)
def update(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update.html', context)
def delete(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task':task}
    return render(request, 'tasks/delete.html', context)





# Create your views here.
