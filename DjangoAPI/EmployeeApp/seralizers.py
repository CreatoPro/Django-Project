from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartmentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                'DepartmentName')

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                'EmployeeName',
                'Department',
                'DateOfJoining',
                'PhotoFileName')