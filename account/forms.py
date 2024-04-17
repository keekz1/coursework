from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

class SignUpForm(UserCreationForm):
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
    approve = forms.BooleanField(label='Approve', required=False)  # Add the "Approve" checkbox

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'approve')  # Include the "approve" field

class CustomUserCreationForm(forms.ModelForm):
    approve = forms.BooleanField(label='Approve', required=False)

    class Meta:
        model = User
        fields = '__all__'
