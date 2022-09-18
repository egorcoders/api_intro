from django.shortcuts import render
from rest_framework import generics
from api.api_app.models import Women

from .serializers import WomenSerializer


#
#
# # Create your views here.
class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    string = """
    SELECT * FROM api_app_category;
    """
