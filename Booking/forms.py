from django import forms
from .models import UnsavedItem, SavedItem

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

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()
