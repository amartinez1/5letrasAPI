from django.contrib import admin

from .models import Room
from .models import RoomImage


class RoomImageChoiceInLine(admin.TabularInline):
    model = RoomImage
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motel', 'name', 'price', 'description',
              'status', 'room_amenities')
    list_display = ('id', 'name', 'motel', 'price',
                    'status', 'updated_date')
    list_display_links = ['id', 'name', 'status']
    list_filter = ['motel', 'price', 'room_amenities',
                   'status']
    search_fields = ['id', 'name', 'slug', 'motel', 'price',
                     'room_amenities', 'status']
    inlines = [RoomImageChoiceInLine]


class RoomImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motels', 'image')
    list_display = ('id', 'motels', 'image',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter = ['id', 'image']
    search_fields = ['id', 'image']

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage, RoomImageAdmin)
