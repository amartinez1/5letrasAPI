from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_date"
    fields = ('motel', 'body', 'rating', 'status')
    list_display = ('id', 'motel','body', 'rating', 
                    'status', 'created_date')
    list_display_links = ['id', 'body', 'status']
    list_filter =['rating', 'status']
    search_fields = ['id', 'motel', 'body', 'rating']

admin.site.register(Comment, CommentAdmin)
