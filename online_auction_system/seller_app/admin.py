from django.contrib import admin

from .models import ProductInformation, ProductImages

@admin.register(ProductInformation)
class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_description','product_base_price','owner','product_verify']
    
@admin.register(ProductImages)    
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product_image','product'] 
