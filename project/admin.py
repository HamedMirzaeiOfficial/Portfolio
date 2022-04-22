from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body',  'created_on',
                    'last_modified', 'active')
    list_filter = ('created_on', 'last_modified', 'active')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'created_on'
    ordering = ('active', 'created_on')
