from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 


urlpatterns = [


  
    path("list/", views.list_view, name="list_without_id"),  # Map the list_view without ID
    path("list/<int:id>/", views.list_view, name="list_view"),  
 
        #Search Engine
    path('search_items/', views.Search_Engine, name='search_items'),
    path('item/<int:item_id>/', views.item_info, name='item'),



    # Map the list_view with ID
    path('delete-item/', views.delete_item, name='delete_item'),
    
    path('', views.home, name='homepage'),
    path('home/', views.home, name='home'),
    path('profile/', views.profilepage, name='profile'),


    path('update_user/', views.profile, name='update-user'),

    

    path('index', views.index, name='index'),
    
    path('item/<int:pk>', views.item, name='item'),

    # URL pattern for adding multiple images

]

# Append the URL patterns for serving static files during development
