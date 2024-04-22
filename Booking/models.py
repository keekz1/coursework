from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "List"

class Image(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

class Item(models.Model):
    lists = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    itemName= models.CharField(max_length=100,default=True)
    itemType = models.CharField(max_length=50,default=True) 
    itemDes = models.CharField(max_length=300)
    itemRentalPeriod = models.CharField(max_length=30,default=True)
    complete = models.BooleanField(default=False)




    def __str__(self):
        return self.itemDes

class UnsavedItem(models.Model):
    itemName= models.CharField(max_length=100,default=True)
    itemType = models.CharField(max_length=50,default=True) 
    itemDes = models.CharField(max_length=300)
    itemRentalPeriod = models.CharField(max_length=30,default=True)
    image = models.ImageField(upload_to='unsaved_item_images/', null=True, blank=True)

class SavedItem(models.Model):
    lists = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    itemName= models.CharField(max_length=100,default=True)
    itemType = models.CharField(max_length=50,default=True) 
    itemDes = models.CharField(max_length=300,default=True)
    itemRentalPeriod = models.CharField(max_length=30,default=True)
    image = models.ImageField(upload_to='saved_images/', null=True, blank=True)

    def __str__(self):
        return self.itemDes
