from django import forms
from .models import Recipe, Category


class RecipeForm(forms.Form):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'steps', 'cooking_time', 'image', 'author']

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