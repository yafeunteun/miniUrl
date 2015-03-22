__author__ = 'yafeunteun'

from django.conf.urls import patterns, url

urlpatterns = patterns('mini_url.views',
    url(r'^add_mini/$', 'add_mini')
)
