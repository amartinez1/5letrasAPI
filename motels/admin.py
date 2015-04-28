from django.contrib import admin
from .models import Town, Motel
# Register your models here.

class TownAdmin(admin.ModelAdmin):
	date_hierarchy="updated_date"
	fields = ('name','latitude','longitude')
	list_display=['name']
	search_fields=['name']

class MotelAdmin(admin.ModelAdmin):
	date_hierarchy="updated_date"
	fields = ('name','town','latitude','longitude','ranking','telephone')
	list_display=['name']
	search_fields=['name']

admin.site.register(Town, TownAdmin)
admin.site.register(Motel, MotelAdmin)
