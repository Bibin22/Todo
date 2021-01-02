from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import HttpResponse, render
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'todolist/index.html', {"todo_items": todo_items})
def add_todo(request):
    # print(request.POST)
    current_date = timezone.now()
    content = request.POST["content"]
    obj = Todo.objects.create(added_date=current_date, text=content)
    print(obj)
    print(obj.id)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)

    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

