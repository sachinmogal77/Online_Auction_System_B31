from rest_framework import serializers
from .models import SuccessAuctions, CancelledAuctions

class SuccessAuctionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SuccessAuctions
        fields = '__all__'

class CancelledAuctionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CancelledAuctions
        fields = '__all__'