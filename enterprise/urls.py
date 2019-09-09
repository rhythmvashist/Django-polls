from django.conf.urls import url

from . import views

app_name = 'enterprise'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<enterprise_id>[0-9]+)/$', views.getjson, name='getjson'),


]