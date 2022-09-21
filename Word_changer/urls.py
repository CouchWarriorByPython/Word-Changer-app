from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='word-app')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('word-app/', include('mainapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
