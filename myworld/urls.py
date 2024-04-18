from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path("", include("Booking.urls")),  # Include main app's URLs
    path("", include("django.contrib.auth.urls")),  # Include authentication URLs
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
