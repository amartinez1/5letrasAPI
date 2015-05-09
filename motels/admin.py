from .models import Comment
from .models import Motel
from .models import Town
from .models import Amenitie
from django.contrib import admin
# Register your models here.

class MotelChoiceInLine(admin.TabularInline):
    model = Motel
    extra = 3

class TownAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'latitude', 'longitude')
    list_display = ('id', 'name', 'latitude', 'longitude')
    list_display_links = ['id', 'name']
    list_filter =['name']
    search_fields = ['name', 'latitude', 'longitude']
    inlines = [MotelChoiceInLine]

class MotelAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('name', 'town', 'number_of_rooms', 
              'latitude', 'longitude', 
              'ranking', 'telephone', 'website', 'email',
              'description', 'amenitie')
    list_display = ('id', 'name', 'latitude', 'longitude', 
                    'ranking','number_of_rooms', 'email', 
                    'website', 'created_date', 'updated_date')
    list_display_links = ['id', 'name', 'ranking']
    list_filter =['name','ranking']
    search_fields = ['name', 'latitude', 'longitude', 'ranking']

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

admin.site.register(Town, TownAdmin)
admin.site.register(Motel, MotelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Amenitie, AmenitieAdmin)


