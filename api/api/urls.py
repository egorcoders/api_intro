from django.contrib import admin
from django.db import router
from django.urls import path, include

from quickstart import views

from rest_framework import routers

my_router = routers.DefaultRouter()

my_router.register(r'users', views.UserViewSet)
my_router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(my_router.urls)),
]
