from django.contrib import admin
from .models import Skill, Project, SoftSkill, WorkExperience

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(SoftSkill)
admin.site.register(WorkExperience)
