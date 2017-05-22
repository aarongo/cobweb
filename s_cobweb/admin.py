# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

# Register your models here.
# 进行注册到管理页面
admin.site.register(Host)
admin.site.register(HostGroup)
admin.site.register(user_profile)

