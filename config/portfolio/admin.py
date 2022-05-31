from django.contrib import admin
from .models import AboutMe, Projects, Skill
# Register your models here.
@admin.register(AboutMe)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email']


@admin.register(Projects)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Skill)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'skills']