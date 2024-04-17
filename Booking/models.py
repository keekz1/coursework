from django.db import models




class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    unsaved_image = models.ImageField(upload_to='unsaved_item_images/', null=True, blank=True)
    saved_image = models.ImageField(upload_to='saved_item_images/', null=True, blank=True)
    
    def __str__(self):
         return self.text
     
     
     
class UnsavedItem(models.Model):
    text = models.CharField(max_length=300)
    image = models.ImageField(upload_to='unsaved_item_images/', null=True, blank=True)

class SavedItem(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='saved_images/', null=True, blank=True)

    def __str__(self):
        return self.text