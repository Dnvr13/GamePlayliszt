from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('create/', views.game_create, name='game_create'),
    path('update/<int:pk>/', views.game_update, name='game_update'),
    path('delete/<int:pk>/', views.game_delete, name='game_delete'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
