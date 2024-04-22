from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Map the list_view without ID
    path("list/", views.list_view, name="list_without_id"),

    # Map the list_view with ID
    path("list/<int:id>/", views.list_view, name="list_view"),
    path('delete-item/', views.delete_item, name='delete_item'),

    # URL pattern for adding multiple images
    path("add_multiple_images/", views.add_multiple_images_view, name="add_multiple_images"),
        path('add_multiple_images/<int:id>/', views.add_multiple_images_view, name='add_multiple_images'),

]

# Append the URL patterns for serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
