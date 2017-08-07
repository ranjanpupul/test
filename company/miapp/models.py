from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TimeStampAbstractModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by',  default=1)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, related_name='%(class)s_updated_by', blank=True, null=True,  default=1)

    class Meta:
        abstract = True


class Company(TimeStampAbstractModel):
    companyName = models.CharField(max_length=50, verbose_name='Company Name')
    comapnyLocation = models.CharField(max_length=100, verbose_name='Company Location')
    totalEmployee = models.IntegerField(default=0, verbose_name='Total Number of Employee')


    def __unicode__(self):
        return self.companyName


class JobOpenings(TimeStampAbstractModel):
    roleName = models.CharField(verbose_name='Job Name', max_length=100,)
    associatedCompany = models.ForeignKey(Company)

    def __unicode__(self):
        return self.roleName + '|' + self.associatedCompany.companyName


class EmployeeDetails(TimeStampAbstractModel):
    company = models.ForeignKey(Company)
    employeeName = models.CharField(verbose_name='Name of Employee', max_length=50,)
    employeeRole = models.CharField(verbose_name='ROle of Employee', max_length=25)
    employeeAge = models.IntegerField(verbose_name='Age of an Employee',)


    def __unicode__(self):
        return self.employeeName + '|' + self.company.companyName

