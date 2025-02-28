from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pivo.views import HomeView #LoginView

urlpatterns = [
    #path('', PublicHomeView.as_view(), name='public_home'),    # Veřejná stránka
    path('home/', HomeView.as_view(), name='home'),            # Stránka pro přihlášené
    #path('login/', LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)