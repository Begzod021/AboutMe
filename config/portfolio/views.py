from django.shortcuts import render
from .models import *
from django.http import FileResponse, JsonResponse
import json
from config.settings import DEBUG
# Create your views here.




def home(request):

    projects = Projects.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'index.html', context)




def project(request):
    data = json.loads(request.body)
    proj = Projects.objects.get(id=data['id'])

    
    ctx = {
        'title': proj.title,
        'text': proj.text,
        'img': proj.image.url,
        'url':proj.url,
    }

    return JsonResponse(ctx, safe=False)




def download(request):
    obj = Resume.objects.get(id=1)
    filname = obj.file_resume.path
    response = FileResponse(open(filname, 'rb'))

    return response

def error(request, exception):
    return render(request, '404.html')