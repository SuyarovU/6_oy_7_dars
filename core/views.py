from django.shortcuts import render, redirect
from .forms import TodoModelForm
from .models import Todo



def index(request): 
    todos = Todo.objects.all()
    print(todos)
    print("index ishladi")
    return render(request, 'core/index.html', {'todos': todos})


def create_todo(request):
    form = TodoModelForm()
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        print("Malumot keldi")
        if form.is_valid():
            print("VAlid ekan")
            form.save()
            return redirect("home")
        else:
            return render(request, 'core/todo_create.html', {'form': form})
    return render(request, 'core/todo_create.html', {"form": form})

def todo_item(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, "core/todo_item.html", {"todo": todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("home")

def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method=="POST":
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "core/edit.html", {"todo": todo})