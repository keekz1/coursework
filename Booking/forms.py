from django import forms
from .models import Item , SavedItem



class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()



class AddItemForm(forms.ModelForm):
    image = forms.ImageField(label="Image", required=True)  # Add image field
    class Meta:
        model = Item
        fields = ['text', 'image']


class SaveForm(forms.Form):
    # Define fields if needed for saving data
    pass


class SavedItemForm(forms.ModelForm):
    class Meta:
        model = SavedItem
        fields = ['text', 'image']



