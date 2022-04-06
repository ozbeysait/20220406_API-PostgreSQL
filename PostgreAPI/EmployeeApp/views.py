from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            departments = Departments.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            department = Departments.objects.get(departmentId=id)
            serializer = DepartmentSerializer(department, many=False)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        department = Departments.objects.get(departmentId=id)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        department = Departments.objects.get(departmentId=id)
        department.delete()
        return JsonResponse({'deleted': True}, status=200)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            employee = Employees.objects.all()
            serializer = EmployeeSerializer(employee, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            employee = Employees.objects.get(employeeId=id)
            serializer = EmployeeSerializer(employee, many=False)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        employee = Employees.objects.get(employeeId=id)
        serializer = EmployeeSerializer(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        employee = Employees.objects.get(employeeId=id)
        employee.delete()
        return JsonResponse({'deleted': True}, status=200)