from django.shortcuts import render
from django.http import Http404
from .models import Todo


# Create your views here.
def index(request):
    all_todos = Todo.objects.all()
    return render(request, 'todoBoard/index.html', {'all_todos': all_todos})


def new(request):
    return render(request, 'todoBoard/createTodo.html')


def edit(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        raise Http404("Todo does not exist")
    return render(request, 'todoBoard/editTodo.html', {'todo': todo})
