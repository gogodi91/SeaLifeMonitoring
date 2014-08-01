from django.conf.urls import patterns, url
from Monitoring import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))
       

