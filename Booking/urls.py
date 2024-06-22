from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='homepage'),
    path('home/', views.home, name='home'),
    path('profile/', views.profilepage, name='profile'),
    path('update_user/', views.profile, name='update-user'),
    path('list/', views.list_view, name='list_without_id'),  # List view without ID
    path('list/<int:id>/', views.list_view, name='list_view'),  # List view with ID
    path('search_items/', views.Search_Engine, name='search_items'),  # Search Engine
    path('item/<int:item_id>/', views.item_info, name='item'),  # Item info
    path('delete-item/', views.delete_item, name='delete_item'),  # Delete item
    path('index', views.index, name='index'),  # Index view
]

# Static and media files serving is usually handled in the project's main urls.py
