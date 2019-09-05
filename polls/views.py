# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
from .models import Question

def deft(requet):
    return HttpResponse("inside polls ")

def index(request):
    ques_list=Question.objects.order_By('-pub_date')[:5]
    output=','.join([q.question_text for q in ques_list])
    return HttpResponse(output)


def visit(request):
    return HttpResponse("hey you are visting the phase 1 project")

def detail(request,question_id):
    return HttpResponse('YOUR ARE LOOKIN AT QUESTIONS %s.'% question_id)

def result(request,question_id):
    return HttpResponse('your are looking at the result of the question %s '% question_id)


def vote (request,question_id):
    return HttpResponse('your are voting on question %s'% question_id)

