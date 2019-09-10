from django.conf.urls import url

from . import views

app_name = 'enterprise'
urlpatterns = [


    url(r'^(?P<enterprise_id>[0-9]+)/$', views.detail, name='detail')


]