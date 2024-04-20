from django.urls import path, include
from . import views

urlpatterns = [
  
    path("list/", views.list_view, name="list_without_id"),  # Map the list_view without ID
    path("list/<int:id>/", views.list_view, name="list_view"),  
 
        #Search Engine
    path('Search-Engine', views.Search_Engine, name='Search_Engine'),


  
   

    
 

]
