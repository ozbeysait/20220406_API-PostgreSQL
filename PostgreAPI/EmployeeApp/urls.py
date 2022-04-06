from django.urls import re_path
from EmployeeApp import views

urlpatterns = [
    re_path(r'^departments/$', views.departmentApi),
    re_path(r'^departments/(?P<id>[0-9]+)/$', views.departmentApi),
    re_path(r'^employees/$', views.employeeApi),
    re_path(r'^employees/(?P<id>[0-9]+)/$', views.employeeApi),
]