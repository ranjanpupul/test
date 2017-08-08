from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import EmployeeDetails, JobOpenings, Company
from .serializers import CompanySerializer
from django.template import loader
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
        Return a json with all values
        """
        response_data =  {}
        info = EmployeeDetails.objects.select_related('JobOpenings').values('id','employeeName','employeeRole',
                                                                            'employeeAge','company__companyName',
                                                                            'company__comapnyLocation',
                                                                            'company__totalEmployee',
                                                                            'jobDetail__roleName',
                                                                            'jobDetail__associatedCompany')
        response_data = list(info)
        response_data = json.dumps(response_data)
        return HttpResponse(response_data, content_type="application/json")

    def post(self,request):
        employename = request.POST.get('employeeName=employename',None)
        role = request.POST.get('employeeRole', None)
        age = request.POST.get('employeeAge', None)
        companyname = request.POST.get('company__companyName', None)
        location = request.POST.get('company__comapnyLocation', None)
        total = request.POST.get('company__totalEmployee', None)
        cinfo = Company()
        cinfo.companyName = companyname
        cinfo.comapnyLocation = location
        cinfo.totalEmployee = total
        cinfo.save()
        einfo = EmployeeDetails()
        einfo.company = cinfo.id
        einfo.employeeAge = age
        einfo.employeeName = employename
        einfo.employeeRole = role
        einfo.save()


class ShowResult(APIView):

    def get(self, request):
        serachresult = {}
        name = request.data.get['name']
        searchvalue = EmployeeDetails.objects.filter(employeeRole__icontains=name).values('employeeRole', 'jobDetail__roleName')
        serachresult = list(serachvalue)
        serachresult = json.dumps(searchvalue)
        return HttpResponse(serachresult, content_type="application/json")
