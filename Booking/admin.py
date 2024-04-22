from django.contrib import admin
from .models import Item, ToDoList

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'lists','itemName','itemType','itemRentalPeriod', 'itemDes', 'complete')  # Include 'id' in list display

admin.site.register(Item, ItemAdmin)
admin.site.register(ToDoList)
