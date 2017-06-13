from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # list_display = ['id', 'author', 'created_at', 'updated_at']
    pass
admin.site.register(Post, PostAdmin)
