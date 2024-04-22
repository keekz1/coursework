from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path("", include("Booking.urls")),  # Include main app's URLs
    path("", include("django.contrib.auth.urls")),  # Include authentication URLs
    
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    
  
