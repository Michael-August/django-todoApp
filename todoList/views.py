from todoList.models import Todo
from django.shortcuts import render, redirect

# Create your views here.

def index(request):

    if request.method == 'POST':
        todo = Todo(
            todo = request.POST['todo']
        )
        todo.save()
        return redirect('/')
    else:
        todos = Todo.objects.all()
        return render(request, 'index.html', {'todos': todos})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
