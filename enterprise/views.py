from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Enterprise, Company, Employee, Address

from django.core import serializers

import json


def get_address(address):
    return {
        'address': address.address,
        'city': address.city,
        'province': address.province,
        'postal_code': address.postal,
        'country': address.country,
        'phone_no': address.phone_no,
    }


def detail(request, enterprise_id):
    enterprise = get_object_or_404(Enterprise, pk=enterprise_id)

    companies = Company.objects.filter(Enterprise__id=enterprise_id)

    # list of dictoinaries
    company_list = []

    for company in companies:
        employees = company.employee_set.all()

        # list of dictoinaries
        employee_list = []

        for employee in employees:
            employee_dict = {
                'name': employee.user.username,
            }
            employee_dict.update(get_address(employee.address))
            employee_list.append(employee_dict)

        company_dict = {
            'name': company.name,
            'employees': employee_list,
        }
        company_dict.update(get_address(company.address))
        company.employees = company.employee_set.all()
        company_list.append(company_dict)

    result = {
        'name': enterprise.name,
        'companies': company_list,
    }
    result.update(get_address(enterprise.address))

    return JsonResponse(result)
