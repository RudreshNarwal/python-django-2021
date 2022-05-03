from django.http import HttpResponse


def projects(request):
    return HttpResponse('Here is our projects')


def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))