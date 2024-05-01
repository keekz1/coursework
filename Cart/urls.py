from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('Cart/', views.cart_summary, name='cart-summary'),
    path('add/', views.cart_add, name='cart-add'),
    path('delete/', views.cart_delete, name='cart-delete'),
    path('historical_index', views.historicalindex, name='historical-index'),


]