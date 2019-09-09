# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


from django.shortcuts import render
from .models import Enterprise,Companies,User

# Create your views here.

def index(request):
    return HttpResponse("<H1>THIS IS THE ENTRPRISE</H1> ")

def getjson(request,enterprise_id):
    return HttpResponse("<H1>THIS IS THE ENTRPRISE-detail</H1> ")
