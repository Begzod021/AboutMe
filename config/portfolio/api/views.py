from portfolio.api.serializers import AboutMeSerializers, ProjectSerializers
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
        