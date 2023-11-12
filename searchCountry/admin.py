from django.contrib.gis import admin
from .models import Country

admin.site.register(Country, admin.ModelAdmin)

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]