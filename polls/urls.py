from django.conf.urls import url
from . import  views

urlpatterns=[

    #this is for polls/
    url(r'^$',views.index,name='index'),

    # polls/5
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),

    #name/5/result

    url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='result'),

    #name/5/vote

    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),

]