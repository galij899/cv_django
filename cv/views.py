from django.shortcuts import render
from .models import Skill, Project, SoftSkill

# Create your views here.

def about(request):
    skills = Skill.objects.filter(type="Python")
    web = Skill.objects.filter(type="Web")
    general = Skill.objects.filter(type="General")
    softs = SoftSkill.objects.all()
    projects = Project.objects.all()

    return render(request, 'cv/about.html', {'skills': skills,
                                             'web': web,
                                             'general': general,
                                             'softs': softs,
                                             'projects': projects})

def skills(request):
    return render(request, 'cv/skills.html')