from django.contrib import admin
from .models import Town, Motel
# Register your models here.

class MotelChoiceInLine(admin.TabularInline):
	model = Motel
	extra = 3

class TownAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'latitude', 'longitude')
    list_display = ('name', 'latitude', 'longitude')
    list_display_links = ['name']
    list_filter =['name']
    search_fields = ['name', 'latitude', 'longitude']
    inlines = [MotelChoiceInLine]


class MotelAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'town', 'latitude', 'longitude',
              'ranking', 'telephone', 'website', 'description')
    list_display = ('name', 'latitude', 'longitude', 'ranking')
    list_display_links = ['name','ranking']
    list_filter =['name','ranking']
    search_fields = ['name', 'latitude', 'longitude', 'ranking']

admin.site.register(Town, TownAdmin)
admin.site.register(Motel, MotelAdmin)
