from django.contrib import admin
from .models import ProductInformation,ProductImages


admin.site.register(ProductInformation)
admin.site.register(ProductImages)
# @admin.register(ProductInformation)
# class ProductInformationAdmin(admin.ModelAdmin):
#     list_display = ['']