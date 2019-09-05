# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse

def deft(requet):
    return HttpResponse("inside polls ")

def index(request):
    return HttpResponse("hello my name is phase 1 project ")

def visit(request):
    return HttpResponse("hey you are visting the phase 1 project")