from django.contrib import admin
from .models import Trainer

# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'types',
        'description',
        'price_per_hour',  
    )
    
admin.site.register(Trainer, TrainerAdmin)