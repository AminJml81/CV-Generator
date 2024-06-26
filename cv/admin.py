from django.contrib import admin

# Register your models here.
from cv import models

@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    date_hierarchy = 'gratudated_date'
    list_display = ('title', 'link', 'gratudated_date')
    search_fields = ('title',)
    
    
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'completion_date'
    list_display = ('title', 'link', 'completion_date')
    search_fields = ('title', 'description')
    
    ordering = ('title',)
    
    
@admin.register(models.Education)
class EducationAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    list_display = ('university', 'degree', 'major')
    search_fields = ('university', 'degree', 'major')
    list_filter = ('degree',)
    ordering = ('-graduation_date',)
    
@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    
    ordering = ('-name',)
    
@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tool)
class ToolAdmin(admin.ModelAdmin):
    pass
