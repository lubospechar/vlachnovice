from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pivo.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)