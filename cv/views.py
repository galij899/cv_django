from django.shortcuts import render
from .models import Skill

# Create your views here.

def about(request):
    skills = Skill.objects.filter(type="Python")
    web = Skill.objects.filter(type="Web")
    general = Skill.objects.filter(type="General")
    return render(request, 'cv/about.html', {"skills": skills,
                                             "web": web,
                                             "general": general})

def skills(request):
    return render(request, 'cv/skills.html')