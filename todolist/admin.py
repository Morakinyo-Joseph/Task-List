from django.contrib import admin
from .models import TodoList, Examples

admin.site.register(TodoList)
admin.site.register(Examples)