from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request,'index.html',context)

def update(request,pk):
    tasks = Task.objects.get(id=pk)

    form = TaskForm(instance=tasks)

    if request.method=='POST':
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form':form
    }

    return render(request,'update.html',context)

def delete(request,pk):
    tasks = Task.objects.get(id=pk)

    if request.method=='POST':
        tasks.delete()
        return redirect('/')

    context = {
        'item':tasks
    }

    return render(request,'delete.html',context)

