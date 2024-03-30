from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="home"),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('create_category/', views.create_category, name='create_category'),
    path('edit_recipe/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:pk>/', views.get_recipe, name='recipe')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)