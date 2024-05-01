from django.db import models
from django_resized import ResizedImageField
from image_cropping import ImageCropField, ImageRatioField
from PIL import Image
from account.models import User
import datetime

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "List"



class Image(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    Image = ResizedImageField(size=[300, 300], quality=75, upload_to='item_images', default='', force_format='WEBP', blank=True)

class Category(models.Model):
    name = models.CharField(max_length = 50)

    def _str_(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'
    
class Item(models.Model):
    name        = models.CharField(max_length=100,default=True)
    category    = models.ForeignKey(Category, on_delete = models.CASCADE, default = '')
    description = models.TextField(max_length=500, default='')
    period      = models.CharField(max_length=30, default= '1 Week')
    img         = ResizedImageField(Image, size=[300, 245], crop=['top', 'right'], quality=75, upload_to="Item_img/", force_format='WEBP', blank=True, default='')
    lists       = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    complete    = models.BooleanField(default=False)

    def _str_(self):
        return self.name





#Customer Profile
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE) # Delete profile when user is deleted
    image = ImageCropField(upload_to='profile_pics', default='avatar.png', blank=True)
    cropping = ImageRatioField('image', '150x150')


    def _str_(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
class Booking(models.Model):
     	# Foreign Key
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=250)
	email = models.EmailField(max_length=250)
	date_ordered = models.DateTimeField(auto_now_add=True)	
	dueDate = models.DateTimeField(default=False)

	
	def _str_(self):
		return f'Order - {str(self.id)}'
     
class BookingItem(models.Model):
	# Foreign Keys
	product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def _str_(self):
		return f'Order Item - {str(self.id)}'

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