from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import EmployeeDetails, JobOpenings, Company
from .serializers import CompanySerializer

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
        info = Company.objects.all()
        serializer =  CompanySerializer(info, many=True)
        return Response(serializer.data)

        pass


    def post(self):
        pass