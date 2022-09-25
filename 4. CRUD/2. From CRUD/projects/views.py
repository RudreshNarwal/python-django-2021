from django.shortcuts import render, redirect

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
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)  # It's gonna prefill our form with the project values
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)  # It will update the specific project
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete.html', context)
