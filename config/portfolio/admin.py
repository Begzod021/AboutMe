from django.contrib import admin
from .models import AboutMe, Projects, Skill, Resume, Work, Education
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



@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'aboutme_information']



@admin.register(Work)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'work_title']


@admin.register(Education)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'education_title']