from django.conf.urls import patterns, url
from monitoring import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_area/$', views.add_area, name='add_area'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_info/$', views.add_info, name='add_info'),
	url(r'^get_info/$', views.get_info, name='get_info'),
	)

