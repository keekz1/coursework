from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
  
    path("list/", views.list_view, name="list_without_id"),  # Map the list_view without ID
    path("list/<int:id>/", views.list_view, name="list_view"),  

  
   

    
 

]
