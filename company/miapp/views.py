from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import EmployeeDetails, JobOpenings, Company
from .serializers import CompanySerializer
import json
# Create your views here.


class ShowAllInformation(APIView):
    """
        View to list all users in the system.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """

    def get(self, request):
        """
        Return a list of all users.
        """
        response_data =  {}
        info = EmployeeDetails.objects.select_related('JobOpenings').values('id','employeeName','employeeRole','employeeAge','company__companyName','company__comapnyLocation','company__totalEmployee')
        response_data = list(info)
        response_data = json.dumps(response_data)
        return HttpResponse(response_data, content_type="application/json")

        pass


    def post(self,request):
        employename = request.data.get('employeeName=employename',None)
        role = request.data.get('employeeRole',None)
        age = request.data.get('employeeAge',None)
        companyname = request.data.get('company__companyName', None)
        key = request.data.get('id',None)

        Einfo = EmployeeDetails.objects.get(key=key)
        if Einfo is not None:            
            Einfo.employeeName=employename
            Einfo.employeeRole=role
            Einfo.employeeAge=age
            Einfo.save()