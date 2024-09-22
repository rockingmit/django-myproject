from django.contrib import admin
from services.models import Service, Feature

# Register your models here.
class SeriviceAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "description")
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "description","status")


admin.site.register(Service,SeriviceAdmin)
admin.site.register(Feature,SeriviceAdmin)