from rest_framework import serializers

from .models import Women

# ?
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('name', 'is_married', 'category')


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('name', 'category')


