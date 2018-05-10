from django.shortcuts import render, get_object_or_404, redirect
import datetime
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
    try:
        description = request.POST['description']
        completion = request.POST['completion']
        due = request.POST['due']
    except KeyError:
        return render(request, 'todoBoard/createTodo.html', {'error_msg': "Invalid data submitted"})
    else:
        if len(str(description)) > 160:
            return render(request, 'todoBoard/createTodo.html', {'error_msg': "description must be <= 160 characters"})
        if len(str(description)) == 0:
            return render(request, 'todoBoard/createTodo.html', {'error_msg': "description must be > 0 characters"})

        if not completion or int(str(completion)) < 0 or int(str(completion)) > 100:
            return render(request, 'todoBoard/createTodo.html', {'error_msg': "completion % must be >= 0 and <= 100"})

        try:
            datetime.datetime.strptime(due, '%Y-%m-%d')
        except ValueError:
            return render(request, 'todoBoard/createTodo.html', {'error_msg': "invalid date"})
        else:
            # everything went well
            todo = Todo(description=description, completion=completion, due=due)
            todo.save()
    return redirect('todoBoard:index')


def edit(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todoBoard/editTodo.html', {'todo': todo})


def editsubmit(request, pk):
    try:
        description = request.POST['description']
        completion = request.POST['completion']
        due = request.POST['due']
    except KeyError:
        return render(request, 'todoBoard/editTodo.html', {'error_msg': "Invalid data submitted"})
    else:
        if len(str(description)) > 160:
            return render(request, 'todoBoard/editTodo.html', {'error_msg': "description must be <= 160 characters"})
        if len(str(description)) == 0:
            return render(request, 'todoBoard/editTodo.html', {'error_msg': "description must be > 0 characters"})

        if not completion or int(str(completion)) < 0 or int(str(completion)) > 100:
            return render(request, 'todoBoard/editTodo.html', {'error_msg': "completion % must be >= 0 and <= 100"})

        try:
            datetime.datetime.strptime(due, '%Y-%m-%d')
        except ValueError:
            return render(request, 'todoBoard/editTodo.html', {'error_msg': "invalid date"})
        else:
            # everything went well
            todo = Todo(description=description, completion=completion, due=due)
            todo.save()
    return redirect('todoBoard:index')


def delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    Todo.objects.filter(id=pk).delete()
    return redirect('todoBoard:index')
