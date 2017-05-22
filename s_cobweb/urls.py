from django.conf.urls import url, patterns
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
                       url(r'^software_tmp', 'software_tmp', name='software_tmp'),
                       url(r'^software_install', 'software_install', name='software_install')
                       )
