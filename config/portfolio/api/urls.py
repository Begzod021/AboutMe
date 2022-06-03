"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Aboutme, Project, get_education, get_work, resume, get_project


urlpatterns = [
    path('about-api/', Aboutme.as_view(), name='About'),
    path('project-api/', Project.as_view(), name='Project' ),
    path('resume-api/', resume, name='resume'),
    path('work-api/', get_work, name='work'),
    path('education-api/', get_education, name='education'),
    path('project-detail/<int:pk>/', get_project, name='get_project'),
]
