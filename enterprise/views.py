# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render


from django.shortcuts import render
from .models import Enterprise,Companies,User,Address,Employee

# Create your views here.

def index(request):
    return HttpResponse("<H1>THIS IS THE ENTRPRISE</H1> ")

def getjson(request,enterprise_id):

    enterp=get_object_or_404(Enterprise,pk=enterprise_id)
    selected_comp=enterp.companies_set.all()

    print('list is printed')

    emp_list=list(selected_comp)

    print('employee list')


    #e_l=Employee.objects.filter(Companies__in=emp_list)

    print(selected_comp)

    for comp in selected_comp:
        try:
            selected_emp=comp.employee_set.all()
            print(selected_emp)
        except:
            print('except ran')

    return HttpResponse("<H1>THIS IS THE ENTRPRISE-detail</H1> ")
