from django.contrib import admin
from .models import Course, Skills


# Register your models here.
# Necesario para poder ver los campos ocultos 'created', 'update'
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register([Course, Skills], AboutAdmin)
