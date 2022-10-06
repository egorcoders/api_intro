from django.http import Http404
from rest_framework import generics, serializers

from .models import Women, Record

# class WomenModel:
#     def __init__(self, name, job):
#         self.name = name
#         self.job = job
#
#
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)

# class CategorySerializer(serializers.Serializer):


#
# def encode():
#     model = WomenModel('Masha', 'Engineer')
#     model_s = CategorySerializer(model)
#     print(model_s.data)
#
#
# encode()

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

#
# class RecordRetrieveView(generics.RetrieveAPIView):
#     serializer_class = RecordSerializer
#
#     def get_object(self):
#         try:
#             return Record.objects.get(id=self.request.query_params['id'])
#         except Record.DoesNotExist:
#             raise Http404()
