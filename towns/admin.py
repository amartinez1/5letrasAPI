from django.contrib import admin

from .models import Town
from .models import TownImage


class TownImageChoiceInLine(admin.TabularInline):
    model = TownImage
    extra = 1


class TownAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'latitude', 'longitude', 'status')
    list_display = ('id', 'name', 'latitude', 'longitude',
                    'status')
    list_display_links = ['id', 'name', 'status']
    list_filter = ['name', 'status']
    search_fields = ['id', 'name', 'position']
    inlines = [TownImageChoiceInLine]


class TownImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('towns', 'image')
    list_display = ('id', 'towns', 'image',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter = ['id', 'image']
    search_fields = ['id', 'image']

admin.site.register(Town, TownAdmin)
admin.site.register(TownImage, TownImageAdmin)
