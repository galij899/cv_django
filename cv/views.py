from django.shortcuts import render

from .models import Skill, Project, SoftSkill, WorkExperience


def about(request):
    backend = Skill.objects.filter(type="backend").order_by("id")
    frontend = Skill.objects.filter(type="frontend").order_by("id")
    ds = Skill.objects.filter(type="ds").order_by("id")
    general = Skill.objects.filter(type="General").order_by("id")
    softs = SoftSkill.objects.all().order_by("id")
    projects = Project.objects.all().order_by("id")
    works = WorkExperience.objects.all().order_by("id")

    return render(request, 'cv/about.html', {'backend': backend,
                                             'frontend': frontend,
                                             'ds': ds,
                                             'general': general,
                                             'softs': softs,
                                             'projects': projects,
                                             'works': works})
