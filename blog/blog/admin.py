from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('title', 'publish')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}