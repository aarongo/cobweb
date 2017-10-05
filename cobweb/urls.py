"""cobweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('s_cobweb.urls')),
]


# urlpatterns = [
#     url(r'^$', small_cobweb.index, name='index'),
#     url(r'^download/', small_cobweb.downloader, name='download'),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^search/', small_cobweb.search),
#     url(r'^inset/',small_cobweb.inset,name='insert_data'),
#     url(r'^insert_bash/',small_cobweb.insert_bash,name='insert_bash'),
#     url(r'^author_login/', small_cobweb.author_login, name='login'),
#
# ]