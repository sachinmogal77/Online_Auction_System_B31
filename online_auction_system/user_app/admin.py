from django.contrib import admin

from .models import User,Country,State,City,BankInformation


admin.site.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id','country_name','country_code']

admin.site.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id','state_name','country']

admin.site.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id','city_name','state']


admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['role','aadhar_card','pan_card','passport_front','passport_back','contact_no','address','city','pincode']

admin.site.register(BankInformation)
class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_name','bank_ifsc_code','bank_address','bank_account_number','branch_name']   