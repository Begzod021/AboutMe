from portfolio.api.serializers import (
    AboutMeSerializers, 
    ProjectSerializers, 
    ResumeSerializers, 
    EducationSerializers,
    WorkSerializers
    )
from rest_framework.views import APIView
from portfolio.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
class Aboutme(APIView):

    def get(self, request):
        about = AboutMe.objects.all()

        serializer = AboutMeSerializers(about, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Project(APIView):

    def get(self, request):
        projects = Projects.objects.all()

        serializer = ProjectSerializers(projects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_project(request, pk):
    project = Projects.objects.get(id=pk)

    serializer = ProjectSerializers(project, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['GET'])
def resume(request):
    resum = Resume.objects.all()
    serializers = ResumeSerializers(resum, many=True)

    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_work(request):
    work = Work.objects.all()
    serializers = WorkSerializers(work, many=True)
    
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_education(request):
    education = Education.objects.all()

    serializers = EducationSerializers(education, many=True)

    return Response(serializers.data, status=status.HTTP_200_OK)