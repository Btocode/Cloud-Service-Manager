# cloud_management/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('subscription.urls')),
    path('services/', include('cloud_services.urls')),
]