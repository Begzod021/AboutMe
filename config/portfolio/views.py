from django.shortcuts import render
from .models import *
from django.http import FileResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')


def download(request):
    obj = Resume.objects.get(id=1)
    filname = obj.file_resume.path
    response = FileResponse(open(filname, 'rb'))

    return response