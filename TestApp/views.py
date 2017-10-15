from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from TestApp.models import User

@api_view(['GET'])
def register(request, name, password):
    return Response(status=200)

@api_view(['GET'])
def auth(request, name, password):
    return Response(status=200)

