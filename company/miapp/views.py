from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import EmployeeDetails, JobOpenings, Company
import json
# Create your views here.


class ShowAllInformation(APIView):

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
        ''' we can increase the number of fields as much as we can'''
        try:
            employename = request.POST.get('employeeName', None)
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
            return HttpResponse('Data Saved Successfully....', content_type="application/json")
        except Exception as e:
            return HttpResponse('Something Went Wrong', content_type="application/json")

'''Serch API that will return the employee name'''


class ShowResult(APIView):

    def get(self, request):
        serachresult = {}
        try:
            name = request.GET['name'] if request.GET['name'] != 'None' else None
            if name:
                searchvalue = EmployeeDetails.objects.filter(employeeRole__icontains=name).values('company__companyName', 'jobDetail__roleName', 'employeeName')
                if searchvalue:
                    serachresult = list(searchvalue)
                    serachresult = json.dumps(serachresult)
                    return HttpResponse(serachresult, content_type="application/json")
                else:
                    return HttpResponse('NO result Matching Your Query...', content_type="application/json")
            else:
                return HttpResponse('NO Result Found...', content_type="application/json")
        except Exception as e:
            return HttpResponse('search Something...', content_type="application/json")

