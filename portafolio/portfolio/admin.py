from django.contrib import admin
from .models import Project


# Register your models here.
# Necesario para poder ver los campos ocultos 'created', 'update'
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Project, ProjectAdmin)
