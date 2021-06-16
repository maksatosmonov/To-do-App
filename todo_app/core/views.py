from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Count



def list_todo(request):
    list_todo = ToDo.objects.all().order_by('due_time')
    
    return render(request, "base.html", {'list_todo' : list_todo})


def create_todo(request):
    context = {}
    form = ToDoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("list_todo")       
    
    context['form'] = form
    return render(request, "create_todo.html", context)


def detail_todo(request, pk):
    try:
        detail_todo = ToDo.objects.get(id=pk)
    except ToDo.DoesNotExist:
        raise Http404('Data does not exist')
    
    return render(request, "detail_todo.html", {'detail_todo': detail_todo})


def update_todo(request, pk):
    list_todo = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=list_todo)
    if request.method =='POST':
        form = ToDoForm(request.POST, instance=list_todo)
        if form.is_valid():
            form.save()
            return redirect("list_todo")
    
    return render(request, "update_todo.html", {"form":form})


def delete_todo(request, pk):
    list_todo = ToDo.objects.get(id=pk)
    list_todo.delete()

    return redirect("list_todo")












