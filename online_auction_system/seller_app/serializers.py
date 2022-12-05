from rest_framework import serializers
from .models import ProductImages, ProductInformation

class ProductInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductInformation
        fields = '__all__'

class ProductImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImages
        fields = '__all__'