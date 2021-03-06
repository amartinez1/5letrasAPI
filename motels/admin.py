from django.contrib import admin

from .models import Motel
from .models import MotelImage
from rooms.models import Room


class MotelChoiceInLine(admin.TabularInline):
    model = Motel
    extra = 3


class MotelRoomsInLine(admin.TabularInline):
    model = Room
    extra = 1


class MotelsImageChoiceInLine(admin.TabularInline):
    model = MotelImage
    extra = 1


class MotelAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'town', 'telephone', 'website',
              'address', 'address2', 'email', 'description',
              'status', 'amenities', 'point')
    list_display = ('id', 'town', 'name',
                    'rating', 'user_count',
                    'email', 'address', 'status',
                    'updated_date')
    list_display_links = ['id', 'name', 'status']
    list_filter = ['rating', 'status', 'amenities', 'town']
    search_fields = ['id', 'name', 'slug',
                     'status', 'rating']
    inlines = [MotelsImageChoiceInLine, MotelRoomsInLine]


class MotelImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motels', 'image')
    list_display = ('id', 'motels', 'image',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter = ['id', 'image']
    search_fields = ['id', 'image']


admin.site.register(Motel, MotelAdmin)
admin.site.register(MotelImage, MotelImageAdmin)
