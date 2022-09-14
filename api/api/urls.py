from django.contrib import admin
from django.urls import path

from api_test import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women', views.WomanAPIView.as_view())
]
