from rest_framework import serializers

from api.api_app.models import Women


# class WomenModel:
#     def __init__(self, name, job):
#         self.name = name
#         self.job = job
#
#
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)

class CategorySerializer(serializers.Serializer):


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