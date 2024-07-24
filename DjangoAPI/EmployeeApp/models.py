from django.db import models

# Create your models here.

class Departments(models.Model):

    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Employees(models.Model):

    EmployeeId = models.AutoField(primary_key=True)
    EmploeeName = models.CharField(max_length=300)
    Department =models.CharField(max_length=500,unique=True)
    DateOfJoing =  models.DateTimeField()
    PhotoFileName = models.CharField(max_length=500)


