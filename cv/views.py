from django.shortcuts import render
from .models import Skill

# Create your views here.

def about(request):
    skills = Skill.objects.all()
    return render(request, 'cv/about.html', {"skills": skills})

def skills(request):
    return render(request, 'cv/skills.html')