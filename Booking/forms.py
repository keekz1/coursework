from django import forms
from multiupload.fields import MultiFileField
from .models import Item, SavedItem


from multiupload.fields import MultiFileField

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()

class AddItemForm(forms.ModelForm):
    image = forms.ImageField(label="Image", required=True)

    class Meta:
        model = Item
        fields = ['itemDes', 'image']

class SaveForm(forms.Form):
    pass

class SavedItemForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)

    class Meta:
        model = SavedItem
        fields = ['itemDes', 'images']



from django import forms
from multiupload.fields import MultiFileField

class AddMultipleImagesForm(forms.Form):
    images = MultiFileField(max_num=10, max_file_size=1024*1024*5)
