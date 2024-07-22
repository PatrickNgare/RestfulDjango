from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Departments,Employees

from .serializers import DepartmentSerializer,EmployeeSerializer

@csrf_exempt
def deparmentApi(request,id=0):

    if request.method == 'GET':
        






