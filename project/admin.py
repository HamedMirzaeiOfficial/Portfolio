from django.contrib import admin
from .models import Project, CategoryProject, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['name', 'email', 'body', 'active']


@admin.register(CategoryProject)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'last_modified')
    list_filter = ('created_on', 'last_modified')
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body',  'created_on',
                    'last_modified', 'active')
    list_filter = ('created_on', 'last_modified', 'active')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    date_hierarchy = 'created_on'
    ordering = ('active', 'created_on')
    inlines = [CommentInline]

