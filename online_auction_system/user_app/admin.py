from django.contrib import admin
from.models import Country,State,City,User,BankInformation

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id','country_name','country_code']
    
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id','state_name', ]
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id','city_name']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','role','username','first_name','last_name','address','pincode','email','city','contact_no']
    
@admin.register(BankInformation)
class BankInformationAdmin(admin.ModelAdmin):
    list_display = ['bank_name','bank_address','branch_name']                
