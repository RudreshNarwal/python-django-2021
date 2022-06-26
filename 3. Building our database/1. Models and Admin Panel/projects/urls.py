from django.urls import path
from . import views

urlpatterns = [
    # projects is function. In last param we have specified name"
    path('', views.projects, name='projects'),
    # "<str:pk> here str is string. pk is name for that (other than str , we can speciffy int as well)"
    path('project/<str:pk>/', views.project, name='project'),
]
