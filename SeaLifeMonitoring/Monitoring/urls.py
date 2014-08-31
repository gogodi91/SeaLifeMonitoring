from django.conf.urls import patterns, url
from Monitoring import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_area/$', views.add_area, name='add_area'))
       

