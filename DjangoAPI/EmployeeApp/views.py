from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Departments,Employees

from .serializers import DepartmentSerializer,EmployeeSerializer

@csrf_exempt
def deparmentApi(request,id=0):

    if request.method == 'GET':

        deparments=Departments.objects.all()
        departments_serializer=DepartmentSerializer(deparments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)


    elif request.method =='POST':

        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("added Record successfuly",safe=False)
        return JsonResponse("failed to add record",safe=False)
     
    elif request.method=='PUT':

        department_data = JSONParser().parse(request)
        deparment=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(deparment,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Scuccesfully",safe=False)
        
        return JsonResponse("failed to update",safe=False)

    
    elif request.method == 'DELETE':

        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Record Deleted Scuccesfully",safe=False)
    

    else:

        return JsonResponse("Invalid request",safe=False)





    

@csrf_exempt
def employeeApi(request,id=0):

    if request.method == 'GET':

        employees=Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)


    elif request.method =='POST':

        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("added Record successfuly",safe=False)
        return JsonResponse("failed to add record",safe=False)
     
    elif request.method=='PUT':

        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Scuccesfully",safe=False)
        
        return JsonResponse("failed to update",safe=False)

    
    elif request.method == 'DELETE':

        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Record Deleted Scuccesfully",safe=False)
    

    else:

        return JsonResponse("Invalid request",safe=False)




