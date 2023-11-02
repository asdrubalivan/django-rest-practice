from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer
from .forms import TodoForm
import logging

_logger = logging.getLogger(__name__)

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated, )


def create_todo(request):
    _logger.info("Creating todo")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            _logger.info("Saved new todo")
            messages.success(request, "Saved")
            return redirect("todo_list")
        _logger.warning("Todo is not valid")
    form = TodoForm()
    return render(request, "todo/create.html", dict(form=form))

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})