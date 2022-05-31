from django.contrib import admin

# Register your models here.
from .models import Contact


@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'name']