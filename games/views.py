from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GameForm
from .models import Game
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator


class GameLoginView(LoginView):
    template_name = "registration/login.html"

class GameLogoutView(LogoutView):
    next_page = '/games/login/'  # redirects here after logout

# ----- Authentication -----
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('game_list')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def game_list(request):
    q = request.GET.get('q', '')
    games = Game.objects.filter(owner=request.user, name__icontains=q).order_by('-created_at')
    paginator = Paginator(games, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'games/game_list.html', {'games': page_obj, 'q': q})

@login_required
def game_create(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        game = form.save(commit=False)
        game.owner = request.user
        game.save()
        messages.success(request, "Game added to your playlist!")
        return redirect('game_list')
    return render(request, 'games/game_form.html', {'form': form, 'game': None})

@login_required
def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk, owner=request.user)
    form = GameForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        messages.success(request, "Game updated successfully!")
        return redirect('game_list')
    return render(request, 'games/game_form.html', {'form': form, 'game': game})

@login_required
def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk, owner=request.user)
    if request.method == 'POST':
        game.delete()
        messages.success(request, "Game removed from playlist!")
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})
