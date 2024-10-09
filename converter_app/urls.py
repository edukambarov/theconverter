from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.show_searches, name='profile'),
    path('category/', views.select_category, name='select_category'),
    path('men_shoes/', views.men_shoes, name='men_shoes'),
    path('women_shoes/', views.women_shoes, name='women_shoes'),
    path('women_t_shirt/', views.women_t_shirt, name='women_t_shirt'),
    path('men_t_shirt/', views.men_t_shirt, name='men_t_shirt'),
    path('men_trousers/', views.men_trousers, name='men_trousers'),
    path('women_trousers/', views.women_trousers, name='women_trousers'),
    path('men_shirt/', views.men_shirt, name='men_shirt'),
    path('women_dress_blouse/', views.women_dress_blouse, name='women_dress_blouse'),
]