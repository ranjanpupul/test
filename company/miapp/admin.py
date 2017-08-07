from django.contrib import admin
from .models import Company, JobOpenings, EmployeeDetails
# Register your models here.

admin.site.register(Company)
admin.site.register(JobOpenings)
admin.site.register(EmployeeDetails)
