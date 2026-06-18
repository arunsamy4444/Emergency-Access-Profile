from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return HttpResponse(f"""
        <h1>Welcome {request.user.username}!</h1>
        <p>Email: {request.user.email}</p>
        <a href="/accounts/profile/">My Profile</a> |
        <a href="/accounts/logout/">Logout</a>
    """)

urlpatterns = [
    path('', home_view),
    path('accounts/', include('accounts.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)