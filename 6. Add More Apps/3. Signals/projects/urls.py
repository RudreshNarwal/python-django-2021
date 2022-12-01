from django.urls import path
from . import views

urlpatterns = [
    # projects is function. In last param we have specified name"
    path('', views.projects, name='projects'),
    # "<str:pk> here str is string. pk is name for that (other than str , we can speciffy int as well)"
    path('project/<str:pk>/', views.project, name='project'),

    path('create-project/', views.createProject, name='create-project'),

    path('update-project/<str:pk>/', views.updateProject, name = 'update-project'),

    path('delete-project/<str:pk>/', views.deleteProject, name = 'delete-project')
]
