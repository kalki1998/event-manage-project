from django import forms
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
