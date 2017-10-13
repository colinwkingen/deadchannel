from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),    
    
    url(r'^(?P<score>[0-9]+)/$', views.score, name='score'),
    
    # ex: /polls/5/results/
    
    url(r'^(?P<nickname>[A-Za-z0-9]+)/nickname/$', views.nickname, name='nickname'),    
    
    url(r'^(?P<nickname>[A-Za-z0-9]+)/profile/$', views.profile, name='profile'),

]

