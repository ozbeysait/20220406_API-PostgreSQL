from django.db import models

# Create your models here.

class Departments(models.Model):
    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=200)

    def __str__(self):
        return self.departmentName


class Employees(models.Model):
    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=200)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    dateOfJoining = models.DateField()

    def __str__(self):
        return self.employeeName