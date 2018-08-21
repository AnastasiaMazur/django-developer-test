from django.contrib import admin

from roadmap.models import Project, Roadmap, Step

admin.site.register(Project)
admin.site.register(Roadmap)
admin.site.register(Step)
