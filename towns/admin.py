from django.contrib import admin

from .models import Town
from .models import TownImage

class TownImageChoiceInLine(admin.TabularInline):
    model = TownImage
    extra = 1

class TownAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'latitude', 'longitude')
    list_display = ('id', 'name', 'latitude', 'longitude')
    list_display_links = ['id', 'name']
    list_filter =['name']
    search_fields = ['id', 'name', 'latitude', 'longitude']
    inlines = [TownImageChoiceInLine]

# Register your models here.
class TownImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('towns', 'image')
    list_display = ('id', 'towns', 'image', 
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter =['id','image']
    search_fields = ['id', 'image']

admin.site.register(Town, TownAdmin)
admin.site.register(TownImage, TownImageAdmin)
