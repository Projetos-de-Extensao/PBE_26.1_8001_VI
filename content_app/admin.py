from django.contrib import admin
from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'creator', 'upload_date', 'views', 'is_public', 'status')
    list_filter = ('content_type', 'is_public', 'status', 'upload_date')
    search_fields = ('title', 'description', 'creator__username')
    readonly_fields = ('upload_date', 'views', 'likes')
    list_editable = ('is_public', 'status')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'content_type', 'creator')
        }),
        ('URLs', {
            'fields': ('file_url', 'thumbnail_url')
        }),
        ('Metadados', {
            'fields': ('views', 'likes', 'is_public', 'status', 'upload_date'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('creator',)
        return self.readonly_fields
