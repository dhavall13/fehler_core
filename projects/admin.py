from django.contrib import admin

from .models import Project, ProjectMembership, Task, Risk


admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(Task)
admin.site.register(Risk)
