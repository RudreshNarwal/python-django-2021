from django.shortcuts import render


def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    # passing message variable
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = None
    for element in projectsList:
        if element['id'] == pk:
            project_obj = element
    return render(request, 'projects/project.html', {'project': project_obj})


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]
