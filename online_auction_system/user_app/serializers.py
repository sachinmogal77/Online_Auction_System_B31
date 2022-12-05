from rest_framework import serializers
from .models import Country, State, City ,User, BankInformation

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
        fields = ('city_name','state_id')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id','role','username','first_name','last_name','email','address','pincode','contact_no','date_joined' )   #                    
        
        
class BankInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BankInformation
        fields = '__all__'         
        
    def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            #WishList.objects.create(user=user)
            return user        