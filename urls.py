__author__ = 'yafeunteun'

from django.conf.urls import patterns, url

urlpatterns = patterns('mini_url.views',
    url(r'^$', 'accueil'),
    url(r'^(?P<code>\w{10})$', 'redir'),
    url(r'^add/$', 'add_mini')
)
