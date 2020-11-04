from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('images/', include('images.urls', namespace='images')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
