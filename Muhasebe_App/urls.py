from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Muhasebe.urls')),  # Corrected 'include' and added comma
    path('admin/', admin.site.urls),
]
