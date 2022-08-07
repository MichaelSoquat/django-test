from django.contrib import admin

from .models import Cars, Manufacturer

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Cars)