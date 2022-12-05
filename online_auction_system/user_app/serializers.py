from rest_framework import serializers
from .models import User, Country,State, City, BankInformation


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BankInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = '__all__'                               