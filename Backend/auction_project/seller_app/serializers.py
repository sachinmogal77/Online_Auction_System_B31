from rest_framework import serializers
from .models import ProductInformation,ProductImages


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class ProductInformationSerializer(serializers.ModelSerializer):
    product_images = serializers.ListField(child=serializers.FileField(),write_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault)
    product_imagess = ProductImagesSerializer(read_only=True,many=True)
    
    class Meta:
        model = ProductInformation
        fields = '__all__'

    def create(self, validated_data):
        product_images = validated_data.pop('product_images')
        product = ProductInformation.objects.create(**validated_data)
        for pro_img in product_images:
            obj = ProductImages.objects.create(product=product,product_images=pro_img)
        return product






