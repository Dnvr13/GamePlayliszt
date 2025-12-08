from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'genre', 'platform', 'link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter game name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
            'platform': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Platform'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Game link (optional)'}),
        }
