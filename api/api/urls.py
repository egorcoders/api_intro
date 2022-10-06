from django.contrib import admin
from django.urls import path
# from api_app.views import WomenAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/women_list/', WomenAPIView.as_view()),
]

New text