from django.contrib import admin
from .models import Complaint
# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'status', 'title']
    list_filter = ['category', 'status']
    search_fields = ['title', 'description']
    ordering = ['-created_at']