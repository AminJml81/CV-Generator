from django.shortcuts import render
from cv import models
# Create your views here.


def cv_view(request):
    context = get_information()
    return render(request, 'index.html', context)


def get_information():
    projects = models.Project.objects.all()
    skills= models.Skill.objects.all()
    skills = reversed(skills)
    tools = models.Tool.objects.all()
    certificates = models.Certificate.objects.all()
    info = models.Info.objects.all()
    education = models.Education.objects.all()
    languages = models.Language.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
        'tools': tools,
        'certificates': certificates,
        'info': info,
        'education': education,
        'languages': languages,
    }
    return context
    