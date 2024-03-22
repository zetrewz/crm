from django.contrib import admin

from development.models import Project, Team, Sprint, Task, Invitation

admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Invitation)
