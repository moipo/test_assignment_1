from .models import Category
from django.contrib.auth.models import User
from django import forms

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts = {"username":""}

        labels = {
        "username": "Логин",
        "password":"пароль",
        }


class CategoryModelForm(forms.ModelForm):
    image = forms.ImageField(label=("Картинка"),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Category
        fields = ["name", "image"]

        labels = {
        "name": "название",
        }

        help_texts = {
        "image":"",
        }
