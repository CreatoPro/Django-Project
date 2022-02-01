from asyncore import read
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pydantic import Json
from rest_framework.parsers import JSONParser
import EmployeeApp
# Create your views here.
from EmployeeApp.models import Departments, Employees
from EmployeeApp.seralizers import DepartmentSerilizer, EmployeeSerilizer
from django.core.files.storage import default_storage

@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerilizer(departments, many = True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerilizer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added Succesfully', safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerilizer(department, data=department_data )
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Updated Successfully!!', safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        department= Departments.objects.get(DepartmentId= id)
        department.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerilizer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerilizer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerilizer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)