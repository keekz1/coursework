from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from multiupload.fields import MultiFileField

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

class SignUpForm(UserCreationForm):
    id = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    is_admin = forms.BooleanField(label='Admin', required=False)
    is_customer = forms.BooleanField(label='Customer', required=False)
    is_employee = forms.BooleanField(label='Employee', required=False)

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password1', 'password2', 'is_admin', 'is_customer', 'is_employee')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('is_admin'):
            user.is_admin = True
        if self.cleaned_data.get('is_customer'):
            user.is_customer = True
        if self.cleaned_data.get('is_employee'):
            user.is_employee = True
        if commit:
            user.save()
        return user
