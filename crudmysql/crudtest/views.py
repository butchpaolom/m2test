from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeopleSerializer
from .models import People
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class PeopleView(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = People.objects.all()

