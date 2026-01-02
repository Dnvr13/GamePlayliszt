from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Redirect root URL to /games/
    path('', RedirectView.as_view(url='/games/', permanent=False)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
