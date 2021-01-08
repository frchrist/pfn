
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('felicite-boy/', admin.site.urls),
    path('', include("posting.urls")),
    path('accounts/', include("users.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
