from django.urls import path,re_path,include
from django.conf import settings
from django.views.static import serve
from . import views
from django.conf.urls.static import static


urlpatterns = [
    

    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('confirm/<str:uidb64>/<str:token>/', views.confirm_email, name='confirm_email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # User Roles
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('customer/', views.my_view, name='customer'),
    path('employee/', views.employee, name='employee'),

    # Admin
    path('admin/', views.admin_page, name='admin_page'),
    path('pending-approval/', views.pending_approval_view, name='pending_approval_view'),
    path('accounts/login/', views.login_view, name='login'),

    # Others
    path('registration-success/', views.registration_success, name='registration_success'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    re_path('Booking/', include('Booking.urls')),
    re_path('Cart/', include('Cart.urls')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)