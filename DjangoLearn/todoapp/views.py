from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos
from django.shortcuts import get_object_or_404
from .todo_form import TodoForm

# Create your views here.
def index(request):
    all_todos = Todos.objects.all()
    return render(request, "todoindex.html", { 'todos': all_todos})

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/todos')
    else:
        form = TodoForm() 
        return redirect('/todos')
    return redirect('/todos')