from rest_framework import serializers
from .models import FeedBack
from rest_framework.response import Response

class FeedBackSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    
   
    class Meta:
        model = FeedBack
        fields = '__all__'

    