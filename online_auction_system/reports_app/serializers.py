from rest_framework import serializers
from .models import SuccessAuctions,CancelledAuctions


class SuccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuccessAuctions
        fields = '__all__'


class CancelledSerializers(serializers.ModelSerializer):
    class Meta:
        model = CancelledAuctions
        fields = '__all__'        
