from django.contrib import admin
from .models import Project
# Register your models here.
#para mostrar las horas en solo texto
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)


