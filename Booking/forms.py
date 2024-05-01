from django import forms
from .models import Item, SavedItem, UnsavedItem,Profile, Image

from multiupload.fields import MultiFileField
from account.models import User
from django_resized import ResizedImageField

class AddItemForm(forms.ModelForm):
    image = forms.ImageField(label="Image")
    rental_period = forms.CharField(label="Rental Period", required=False)  # Add rental period field

    class Meta:
        model = UnsavedItem
        fields = ['name', 'type', 'description', 'rental_period', 'image']  # Include rental period field

    def __init__(self, *args, **kwargs):
        super(AddItemForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True  # Ensure image field is required


class SavedItemForm(forms.ModelForm):
    class Meta:
        model = SavedItem
        fields = ['name', 'type', 'description', 'image']







class AddItemForm(forms.ModelForm):
    image = forms.ImageField(label="Image", required=True)

    class Meta:
        model = Item
        fields = ['description', 'image']

class SaveForm(forms.Form):
    pass

class SavedItemForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

    class Meta:
        model = SavedItem
        fields = ['description', 'images']





class AddMultipleImagesForm(forms.Form):
    images = MultiFileField(max_num=10, max_file_size=1024*1024*5)



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    img = ResizedImageField(Image, size=[150, 150], crop=['top', 'right'], quality=75, upload_to="Item_img/", force_format='WEBP', blank=True, )
    class Meta:
        model = Profile
        fields = ['image']


class bookItemForm(forms.ModelForm):
    item_id = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))    
    class Meta:
        model = Profile
        fields = ['image']


