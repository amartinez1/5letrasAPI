from django.contrib import admin

from .models import Amenitie
from .models import Comment
from .models import Motel
from .models import MotelImage
from rooms.models import Room

class MotelChoiceInLine(admin.TabularInline):
    model = Motel
    extra = 3

class MotelRoomsInLine(admin.TabularInline):
    model = Room
    extra = 3

class MotelsImageChoiceInLine(admin.TabularInline):
    model = MotelImage
    extra = 1

class MotelAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'town', 'number_of_rooms', 
              'latitude', 'longitude', 'telephone', 
              'website', 'address', 'address2', 
              'email','description', 'amenities')
    list_display = ('id', 'name', 'latitude', 'longitude', 
                    'ranking', 'number_of_rooms', 'email', 
                    'address', 'updated_date')
    list_display_links = ['id', 'name', 'ranking']
    list_filter =['name','ranking']
    search_fields = ['name', 'latitude', 'longitude', 'ranking']
    inlines = [MotelsImageChoiceInLine, MotelRoomsInLine]

class MotelImageAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motels', 'image')
    list_display = ('id', 'motels', 'image',
                    'created_date', 'updated_date')
    list_display_links = ['id', 'image']
    list_filter =['id','image']
    search_fields = ['id', 'image']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motel', 'body', 'ranking')
    list_display = ('id', 'body', 'ranking', 'created_date')
    list_display_links = ['id', 'body', 'ranking']
    list_filter =['body','ranking']
    search_fields = ['body', 'ranking']

class AmenitieAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name',)
    list_display = ('id', 'name')
    list_display_links = ['id', 'name']
    list_filter =['name']
    search_fields = ['name']

admin.site.register(Motel, MotelAdmin)
admin.site.register(MotelImage, MotelImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Amenitie, AmenitieAdmin)
