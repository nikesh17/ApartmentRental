from django.contrib import admin
from .models import User


# Register your models here.

admin.site.site_header = 'Apartment Rental'
class UserAdmin(admin.ModelAdmin):
        list_display=('username','email','first_name','last_name','phone_number','date_of_birth','gender')

admin.site.register(User, UserAdmin)