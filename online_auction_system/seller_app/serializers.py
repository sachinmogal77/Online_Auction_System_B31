from rest_framework import serializers
from .models import ProductInformation, ProductImages


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'        