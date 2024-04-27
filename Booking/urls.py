from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 



urlpatterns = [


  
    path("list/", views.list_view, name="list_without_id"),  # Map the list_view without ID
    path("list/<int:id>/", views.list_view, name="list_view"),  
 
        #Search Engine
    path('Search-Engine', views.Search_Engine, name='Search_Engine'),



    # Map the list_view with ID
    path('delete-item/', views.delete_item, name='delete_item'),

    # URL pattern for adding multiple images

]

# Append the URL patterns for serving static files during development
