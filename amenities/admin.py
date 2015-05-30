from django.contrib import admin

from .models import Amenitie


class AmenitieAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name',)
    list_display = ('id', 'name', 'created_date')
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['id', 'name', 'slug']


admin.site.register(Amenitie, AmenitieAdmin)
