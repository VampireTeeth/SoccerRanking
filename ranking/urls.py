'''
Created on Oct 1, 2012

@author: steven
'''
from django.conf.urls import url, patterns

urlpatterns = patterns('ranking.views',
                       url(r'^$', 'index'),
                       url(r'^add/$', 'add'),
                       url(r'^update/(\d+)/$', 'update'),
                       )
