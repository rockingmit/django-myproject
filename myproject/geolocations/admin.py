from django.contrib import admin
from geolocations.models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "status")
class CityAdmin(admin.ModelAdmin):
    list_display = ("name","state","country","status")

admin.site.register(Country,CountryAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)