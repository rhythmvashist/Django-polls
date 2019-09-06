# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Question,Chocie
from django.urls import reverse

from django.template import  loader


def index(request):
    ques_list=Question.objects.order_by('-pub_date')[:5]

    params={
        'ques_list':ques_list,
    }
    print("this is index")
    print (params)
    return render(request,'polls/index.html',params)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("detail")
    print(question)
    print(question.chocie_set.all)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.chocie_set.get(pk=request.POST['chocie'])
    except (KeyError, Chocie.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



