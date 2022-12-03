from django.contrib import admin
from . import models

admin.site.register(models.Country)
admin.site.register(models.State)
admin.site.register(models.City)
admin.site.register(models.User)
admin.site.register(models.BankInformation)