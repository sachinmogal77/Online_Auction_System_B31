from rest_framework import serializers
from .models import User, Country, City, State
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    city = serializers.CharField(max_length= 30)
    state = serializers.CharField(max_length = 40, write_only = True)
    country = serializers.CharField(max_length = 40, write_only = True)
    code = serializers.CharField(max_length = 10, write_only = True)
    contact_no = PhoneNumberField()
    confirm_password = serializers.CharField(max_length= 80, write_only = True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password','confirm_password', 'email', 'contact_no', 'country','code', 'state', 'address','city', 'pincode']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password1 = attrs.get('confirm_password')
        if not password ==password1:
            raise serializers.ValidationError('Password and Confirm Password should be same')
        return attrs

    def create(self, validated_data):
        country = validated_data.pop('country')
        code = validated_data.pop('code')
        state = validated_data.pop('state')
        city = validated_data.pop('city')
        password1 = validated_data.pop('confirm_password')

        c, created = Country.objects.get_or_create(country_name = country, country_code = code)
        state, screated = State.objects.get_or_create(state_name = state, country = c or created)
        city, citycreated = City.objects.get_or_create(city_name = city, state = state or screated)
        return User.objects.create_user(**validated_data, city=city or citycreated)


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=100,required = True)
    new_password = serializers.CharField(max_length=100,required = True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class SatteSerializer(serializers.ModelSerializer):
    cities = CitySerializer(read_only = True, many=True)
    class Meta:
        model = State
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    states = SatteSerializer(read_only = True, many=True)
    class Meta:
        model = Country
        fields = '__all__'