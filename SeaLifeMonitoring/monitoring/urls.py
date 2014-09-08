from django.conf.urls import patterns, url
from monitoring import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_area/$', views.add_area, name='add_area'),
	url(r'^add_vessel/$', views.add_vessel, name='add_vessel'),
	url(r'^add_cruise/$', views.add_cruise, name='add_cruise'),
	url(r'^add_station/$', views.add_station, name='add_station'),
	url(r'^add_typespec/$', views.add_typespec, name='add_typespec'),
	url(r'^add_taxa/$', views.add_taxa, name='add_taxa'),
	url(r'^add_chemparam/$', views.add_chemparam, name='add_chemparam'),
	url(r'^add_event/$', views.add_event, name='add_event'),
	url(r'^add_chemistry/$', views.add_chemistry, name='add_chemistry'),
	url(r'^add_dataab/$', views.add_dataab, name='add_dataab'),
	url(r'^add_sizeagefish/$', views.add_sizeagefish, name='add_sizeagefish'),
	url(r'^add_age/$', views.add_age, name='add_age'),
	url(r'^add_size/$', views.add_size, name='add_size'),
	url(r'^add_note/$', views.add_note, name='add_note'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_info/$', views.add_info, name='add_info'),
	url(r'^get_info/$', views.get_info, name='get_info'),
	url(r'^results/$', views.results, name='results'),
	)

