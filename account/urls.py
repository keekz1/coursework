from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Keep only one of these
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('confirm/<str:uidb64>/<str:token>/', views.confirm_email, name='confirm_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/', views.admin_page, name='admin_page'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('pending-approval/', views.pending_approval_view, name='pending_approval_view'), 
    path('logout/', views.logout_view, name='logout'),
]

# Add this if you are serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
