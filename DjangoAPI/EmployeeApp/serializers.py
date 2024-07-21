from rest_framework import serializers

from . models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Departments
        fields=('DepartmentID','DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoing','PhotoFileName')
