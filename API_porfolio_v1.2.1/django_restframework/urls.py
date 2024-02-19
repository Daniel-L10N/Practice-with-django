from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('docs/', include_docs_urls(title = "API Documentation"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)