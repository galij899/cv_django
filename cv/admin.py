from django.contrib import admin

from .models import Skill, Project, SoftSkill, WorkExperience

for model in [Skill, Project, SoftSkill, WorkExperience]:
    admin.site.register(model)
