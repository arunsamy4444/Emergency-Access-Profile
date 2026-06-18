from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('generate-qr/', views.generate_qr_view, name='generate_qr'),
    path('download-qr/', views.download_qr_view, name='download_qr'),
    path('public/<uuid:uuid>/', views.public_profile_view, name='public_profile'),
    path('log-scan/<uuid:uuid>/', views.log_scan_view, name='log_scan'),
]