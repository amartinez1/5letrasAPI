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
    fields = ('name', 'town', 'latitude', 'longitude', 
              'telephone', 'website', 'address', 'address2', 
              'email','description', 'status','amenities')
    list_display = ('id', 'town', 'name', 'latitude', 'longitude', 
                    'rating', 'email', 'address', 'status', 'updated_date')
    list_display_links = ['id', 'name', 'status']
    list_filter =['rating', 'status', 'amenities', 'town']
    search_fields = ['id', 'name', 'slug', 'latitude', 
                     'longitude', 'status', 'rating']
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
    fields = ('motel', 'body', 'rating', 'status')
    list_display = ('id', 'motel','body', 'rating', 
                    'status', 'created_date')
    list_display_links = ['id', 'body', 'status']
    list_filter =['rating', 'status']
    search_fields = ['id', 'motel', 'body', 'rating']

class AmenitieAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name',)
    list_display = ('id', 'name', 'created_date')
    list_display_links = ['id', 'name']
    list_filter =['name']
    search_fields = ['id', 'name', 'slug']

admin.site.register(Motel, MotelAdmin)
admin.site.register(MotelImage, MotelImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Amenitie, AmenitieAdmin)
