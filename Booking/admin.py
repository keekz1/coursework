from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import ToDoList, Item




admin.site.register(ToDoList)
admin.site.register(Item)


