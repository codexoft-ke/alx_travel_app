from django.contrib import admin
from .models import Listing

# Register your models here.

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """
    Admin configuration for Listing model
    """
    list_display = ('title', 'location', 'price_per_night', 'created_by', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'location')
    search_fields = ('title', 'location', 'description')
    list_editable = ('is_active',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'location')
        }),
        ('Pricing', {
            'fields': ('price_per_night',)
        }),
        ('Management', {
            'fields': ('created_by', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
