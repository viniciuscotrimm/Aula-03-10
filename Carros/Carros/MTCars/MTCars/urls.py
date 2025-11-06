"""
URL configuration for MTCars project.

[...]
"""

from django.contrib import admin
from django.urls import path
from django.urls import include # 1. ADICIONE ESTA LINHA (como no roteiro)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("CarsApp.urls")),  # 2. ADICIONE ESTA LINHA (como no roteiro)
]