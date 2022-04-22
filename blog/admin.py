from django.contrib import admin
from .models import Post, Category, Advertise


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'created_on',
                    'last_modified', 'category', 'active')
    list_filter = ('created_on', 'last_modified', 'category', 'active')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_on'
    ordering = ('active', 'created_on')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image',
                    'created_on', 'last_modified', 'active')
    list_filter = ('created_on', 'last_modified', 'active')
