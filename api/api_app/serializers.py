from rest_framework import serializers

class WomenModel:
    def __init__(self, name, job):
        self.name = name
        self.job = job


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


def encode():
    model = WomenModel('Masha', 'Engineer')
    model_s = CategorySerializer(model)
    print(model_s.data)


encode()