from django.shortcuts import render
from .models import *
from django.http import FileResponse, JsonResponse
# Create your views here.




def home(request):

    projects = Projects.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'index.html', context)




def project(request):

    pk = request.GET.get('id')

    proj = Projects.objects.get(id=pk)

    return JsonResponse(proj)




def download(request):
    obj = Resume.objects.get(id=1)
    filname = obj.file_resume.path
    response = FileResponse(open(filname, 'rb'))

    return response