from django.contrib import admin

from .models import Room
from .models import RoomImage

class RoomImageChoiceInLine(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'motel', 'price',
    		  'description', 'amenitie')
    list_display = ('id', 'name', 'motel', 
                    'price', 'updated_date')
    list_display_links = ['id', 'name']
    list_filter =['name','motel']
    search_fields = ['name', 'motel']
    inlines = [RoomImageChoiceInLine]

class RoomImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motels', 'image')
    list_display = ('id', 'motels', 'image',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter =['id','image']
    search_fields = ['id', 'image']

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage, RoomImageAdmin)