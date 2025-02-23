from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):
    items_ordering = Todo.objects.order_by('-date')
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Saved Successfully!!!")
            form = TodoForm()
        else:
            print(form.errors)
    else:
        form = TodoForm()
    context = {
        'form': form,
        'items': items_ordering
    }
    return render(request, 'index.html', context)

def remove(request, items_id):
    items = Todo.objects.get(id=items_id)
    items.delete()
    messages.success(request, "Items Deleted Successfully!!!")
    return redirect('todo_index')
