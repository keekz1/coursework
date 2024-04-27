from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "List"

class Item(models.Model):
    lists = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100, default='')  # Add default value for 'name'
    type = models.CharField(max_length=50, default='')   # Add default value for 'type'
    description = models.CharField(max_length=300, default='')  # Add default value for 'description'
    rental_period = models.CharField(max_length=30, blank=True, null=True)
    complete = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"Image for {self.item.name}"


class UnsavedItem(models.Model):
    name = models.CharField(max_length=100, default='')  # Add default value for 'name'
    type = models.CharField(max_length=50, default='')   # Add default value for 'type'
    description = models.CharField(max_length=300, default='')  # Add default value for 'description'
    rental_period = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='unsaved_item_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class SavedItem(models.Model):
    lists = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='saved_items')
    name = models.CharField(max_length=100, default='')  # Add default value for 'name'
    type = models.CharField(max_length=50, default='')   # Add default value for 'type'
    description = models.CharField(max_length=300, default='')  # Add default value for 'description'
    rental_period = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='saved_images/', null=True, blank=True)

    def __str__(self):
        return self.name
