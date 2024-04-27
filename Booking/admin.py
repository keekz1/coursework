from django.contrib import admin
from .models import Item, ToDoList

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'lists','image','name','type','rental_period', 'description', 'complete')  # Include 'id' in list display

admin.site.register(Item, ItemAdmin)
admin.site.register(ToDoList)
