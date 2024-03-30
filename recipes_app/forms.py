from django import forms
from .models import Recipe, Category


class RecipeForm(forms.Form):
    name = forms.CharField(max_length=42, widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput())
    steps = forms.CharField(widget=forms.TextInput())
    cooking_time = forms.IntegerField(widget=forms.TextInput())
    image = forms.ImageField()
    author = forms.CharField(widget=forms.TextInput())

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)