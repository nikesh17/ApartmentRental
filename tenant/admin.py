from django.contrib import admin
from .models import Apartment
# Register your models here.


class ApartmentAdmin(admin.ModelAdmin):
        list_display=('apartment_id','location','price','description','image','is_available')
        
admin.site.register(Apartment,ApartmentAdmin)
