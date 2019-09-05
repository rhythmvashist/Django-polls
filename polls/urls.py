from django.conf.urls import url
from . import  views

urlpatterns=[
    url('',views.deft,name='defaultpolls'),
    url(r'^$',views.index,name='index'),
    url(r'^$',views.visit,name='visit'),
    url(r'^$',views.index,name='index'),
    ]