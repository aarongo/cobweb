from django.conf.urls import url
from s_cobweb.views import *

urlpatterns = [
   url(r'^$', index, name='index'),
   url(r'^login/', author_login, name='login'),
   url(r'^logout', author_logout, name='logout'),
   url('^register/$', RegisterView.as_view(), name='register'),
   url(r'^assets_info/', assets_info, name='assets_info'),
   url(r'^supervisor_json', supervisor_json, name='supervisor_json'),
   url(r'^process_info', process_info, name='process_info'),
   url(r'^information_detail/$', information_detail, name='information_detail'),
   url(r'^process_stop/(.+)/$', process_stop, name='process_stop'),
   url(r'^process_start/(.+)/$', process_start, name='process_start'),
   url(r'^process_restart/(.+)/$', process_restart, name='process_restart'),
   url(r'^assets_json', assets_json, name='assets_json'),
   url(r'^add_data', add_data, name='add_data')
]