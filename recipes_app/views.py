from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import RecipeForm, CategoryForm, LoginForm, RegisterForm
from .models import Recipe, Category, RecipeCategory


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes_app/index.html', {'recipes': recipes})

def get_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    categories = RecipeCategory.objects.filter(recipe=recipe)
    
    context = {
        'recipe': recipe,
        'categories': categories
    }
    return render(request, 'recipes_app/recipe_detail.html', context)

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана!')
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'recipes_app/categories_form.html', {'form': form})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, 'Рецепт успешно создан!')
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes_app/recipe_form.html', {'form': form})

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно изменена!')
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes_app/edit_recipe.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('home')
            else:
                messages.error(request, 'Пользователь не найден!')
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'recipes_app/login_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Пользователь успешно создан!!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'recipes_app/registration_form.html', {'form': form})

def logout_view(request):
    if request.session.is_empty():
        messages.error(request, 'Прежде чем выйти из аккаунта вы должны войти или зарегестрироваться!')
        return redirect('home')
    messages.success(request, 'Вы успешно вышли из аккаунта!')
    logout(request)
    return redirect('home')