from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponse

def index(request):
    todos = Todo.objects.filter(title__contains= request.GET.get('search', ''))
    context = {
        'section': 'Tareas',
        'todos': todos,
    }
    return render(request, 'todo/index.html', context)

def view(request, id):
    if request.method == 'GET':    
        todo = Todo.objects.get(id = id)
        context = {
            'section': 'Tarea',
            'todo': todo,
        }
        return render(request, 'todo/dateil.html', context)

def edit(request, id):
    todo = Todo.objects.get(id=id)
    if (request.method == 'GET'):
        form = TodoForm(instance= todo)
        context = {
            'section': 'Edit',
            'form': form,
            'id': id
        }
        return render(request, 'todo/edit.html', context)
    elif (request.method == "POST"):
        form = TodoForm(request.POST, instance= todo)
        if form.is_valid():
            form.save()
        
        context =  {
            'form': form,
            'id': id
        }
        messages.success(request, 'Tarea actualizada con exito!')
        return render(request, 'todo/edit.html', context)
    else:
        return HttpResponse("A ocurrido algun error, porfavor reintente luego")
def delete(request, id):
    if request.method == "GET":
        todo = Todo.objects.get(id = id)
        todo.delete()
        return redirect('todo')
def create(request):
    if (request.method == 'GET'):
        form = TodoForm()
        section = 'Create'
        context = {
            'form': form,
            'section': section
        }
        return render(request, 'todo/create.html', context)
    elif request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        # messages.success(request, 'Contacto creado con exito!')
        return redirect('todo')
    else:
        return HttpResponse("A ocurrido un Error")