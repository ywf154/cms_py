from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from NEVMS import settings


urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
