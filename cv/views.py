from django.shortcuts import render
from .models import Skill, Project, SoftSkill
from django.utils.translation import get_language

# Create your views here.

def about(request):
    backend = Skill.objects.filter(type="backend").order_by("id")
    frontend = Skill.objects.filter(type="frontend").order_by("id")
    ds = Skill.objects.filter(type="ds").order_by("id")
    general = Skill.objects.filter(type="General").order_by("id")
    softs = SoftSkill.objects.all().order_by("id")
    projects = Project.objects.all().order_by("id")

    return render(request, 'cv/about.html', {'backend': backend,
                                             'frontend': frontend,
                                             'ds': ds,
                                             'general': general,
                                             'softs': softs,
                                             'projects': projects})

def skills(request):
    return render(request, 'cv/skills.html')