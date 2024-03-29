from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('accounts.urls')), 
    path('movies/', include('movies.urls')), 
    # path('', include('movies.urls')), 
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
