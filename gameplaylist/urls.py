from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Redirect root URL to /games/
    path('', RedirectView.as_view(url='/games/', permanent=False)),
]
