from django.contrib import admin

# Register your models here.
from blog.models import Comment

# Register your models here.

#admin.site.register(Product)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')
    list_filter = ('created_date')
    search_fields = ('author', 'text')
    actions = ['approve_comments']