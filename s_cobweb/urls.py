from django.conf.urls import patterns, url

from s_cobweb.views import RegisterView

urlpatterns = patterns('s_cobweb.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^login/', 'author_login', name='login'),
                       url(r'^logout', 'author_logout', name='logout'),
                       url('^register/$', RegisterView.as_view(), name='register'),
                       url(r'^search/', 'search', name='search'),
                       url(r'^return_data', 'return_data', name='return_data'),
                       url(r'^submit_data', 'submit_data', name='submit_data'),
                       url(r'^submit_tmp', 'submit_tmp', name='submit_tmp'),
                       url(r'^socket_test', 'view_realy', name='socket_test'),
                       url(r'^supervisorjson', 'supervisorjson', name='supervisorjson'),
                       url(r'^process_info', 'process_info', name='process_info'),
                       url(r'^getdetail/(.+)/$', 'getdetail', name='getdetail'),
                       url(r'^stopprocess/(.+)/$', 'stopprocess', name='stopprocess'),
                       url(r'^startprocess/(.+)/$', 'startprocess', name='startprocess'),
                       url(r'^restartprocess/(.+)/$', 'restartprocess', name='restartprocess'),
                       )
