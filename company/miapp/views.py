from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import EmployeeDetails, JobOpenings

# Create your views here.


class ShowAllInformation(APIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        employeevalue = EmployeeDetails.objects.all().values('company', 'employeeName', 'employeeRole',
                                                                'employeeAge', 'company__companyName',
                                                                'company__comapnyLocation',
                                                                'company__totalEmployee', 'job__roleName')
        return Response(employeevalue)