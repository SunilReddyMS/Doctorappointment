from django.contrib import admin

from .models import contactus

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
     list_display = ['name', 'number', 'email', 'options','options','message','upload']



admin.site.register(contactus, contactusAdmin)  