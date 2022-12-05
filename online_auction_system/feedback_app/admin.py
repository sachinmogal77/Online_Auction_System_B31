from django.contrib import admin
from .models import FeedBack

@admin.register(FeedBack)    
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['email','response','feedback_date'] 
