from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women


# from .serializers import WomenSerializer

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     def get(self, request):
#         posts = Women.objects.all().values()
#         return Response({'posts': list(posts)})
#
#     def post(self, request):
#         post = Women.objects.create(
#             name=request.data['name'],
#             is_married=request.data['is_married'],
#             category_id=request.data['category_id'],
#         )
#         return Response({'post': model_to_dict(post)})





class WomanAPIView(APIView):
    def get(self, request):
        usernames = [username.name for username in Women.objects.all()]
        return Response(usernames)










