from todo.models import Todo, STATUS_CHOICES
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from typing import List, Dict


def get_all_todos() -> QuerySet:
   return  Todo.objects.all().order_by('date')

def get_todo_by_pk(pk:str or int) -> Todo:
   return get_object_or_404(Todo, pk=pk)

def get_status_choices() -> List:
   return STATUS_CHOICES

def create_todo_task(todo: Dict):
   Todo.objects.create(**todo)
