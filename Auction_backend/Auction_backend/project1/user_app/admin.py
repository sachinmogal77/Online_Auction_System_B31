from django.contrib import admin
from .models import Country, State, City, User, BankInformation
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','role','username','password','contact_no', 'address','pincode')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_name', 'country_code')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'city_name')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name') 