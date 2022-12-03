from rest_framework import serializers
from .models import User,Country,State,City,BankInformation


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = '__all__'


