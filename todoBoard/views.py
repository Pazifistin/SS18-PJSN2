from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Todo


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'todoBoard/index.html', {'all_todos': all_todos})


# returns the createTodo.html
def new(request):
    return render(request, 'todoBoard/createTodo.html')


# gets called when the submit button is hit on the createTodo.html
def newsubmit(request):
    description = request.POST['description']
    return redirect('')


def edit(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todoBoard/editTodo.html', {'todo': todo})


def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    Todo.objects.filter(id=pk).delete()
    return redirect('')
