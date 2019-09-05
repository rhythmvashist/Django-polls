# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Question,Chocie
from django.urls import reverse

from django.template import  loader


def index(request):
    ques_list=Question.objects.order_By('-pub_date')[:5]

    params={
        'ques_list':ques_list,
    }

    return render(request,'polls/index.html',params)


def detail(request,question_id):
    try:
        ques=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question deos not exist")

    return render(request,'polls/detail.html',{'ques':ques})

def result(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return  render(request,'polls/result.html',pk=question_id)


def vote (request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.chocie_set.get(pk=request.POST['Chocie'])
    except(KeyError,Chocie.DoesNotExist):
        param={
            'question':question,
            'error_message':'you didnt select any choie please procced by selecting a choice ',
        }
        return  render(request,'polls/detail.html',param)
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponse(reverse('polls:result',args=(question.id)))



