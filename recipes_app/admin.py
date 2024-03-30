from django.contrib import admin
from .models import Recipe, Category, RecipeCategory

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'steps', 'cooking_time', 'image', 'author']
    list_filter = ['author']
    search_fields = ['name', 'author']

    fieldsets = [
        (
        None,
        {
            'classes': ['wide'],
            'fields': ['name'],
        },
    ),
    (
        "Информация р рецепте",
        {
            'classes': ['collapse'],
            'description': 'Описание, шаги и время приготовления, картинка, автор',
            'fields': ['description', 'steps', 'cooking_time', 'image', 'author'],
        },
    )]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

    fieldsets = [
        (
        None,
        {
            'classes': ['wide'],
            'fields': ['name'],
        },
    )]

class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'category']

    fieldsets = [
        (
        None,
        {
            'classes': ['wide'],
            'fields': ['recipe'],
            },
    ),
    (
            "Категория",
        {
            'classes': ['wide'],
            'fields': ['category']
        },
    )]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
