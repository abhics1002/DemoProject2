from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.http import httpResponse

class PersonViewSet(viewsets.ViewSet):

    def GetAllPersons(self, request):
        #query table for all persion
        return Http
