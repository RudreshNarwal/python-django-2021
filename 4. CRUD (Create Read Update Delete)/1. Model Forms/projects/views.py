from django.shortcuts import render

from projects.models import Project


def projects(request):
    projects = Project.objects.all()  # Get all projects
    context = {'projects': projects}
    # passing message variable
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'project': project_obj})


def create_project(request):
    context = {}
    return render(request, 'projects/project_form.html', context)
