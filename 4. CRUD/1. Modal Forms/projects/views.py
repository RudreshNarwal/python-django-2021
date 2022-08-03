from django.shortcuts import render

from projects.models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()  # Get all projects
    context = {'projects': projects}
    # passing message variable
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'project': project_obj})


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)
