from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Company, EmployeeDetails


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmployeeDetails
		fields = '__all__'