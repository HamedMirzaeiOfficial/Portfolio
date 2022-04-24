from django.contrib import admin
from .models import Post, Category, Advertise, Comment, Contact


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['name', 'email', 'body', 'active']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'created_on',
                    'last_modified', 'category', 'active')
    list_filter = ('created_on', 'last_modified', 'category', 'active')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_on'
    search_fields = ['name', 'body']
    ordering = ('active', 'created_on')
    inlines = [CommentInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')
    search_fields = ['name']


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image',
                    'created_on', 'last_modified', 'active')
    list_filter = ('created_on', 'last_modified', 'active')
    search_fields = ['title', 'body']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'email', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'body']
