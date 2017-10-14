# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin


# class BookAdmin(ImportExportActionModelAdmin):
#     pass
#
#
# class HostResource(resources.ModelResource):
#     class Meta:
#         model = Host
#         skip_unchanged = True
#         report_skipped = False
#         fields = ('name', 'address', 'mem_total', 'cpu_total', 'os_type', 'disk_total', 'group_name')
#         export_order = ('name', 'address', 'mem_total', 'cpu_total', 'os_type', 'disk_total', 'group_name')
#

class HostResource(ModelResource):
    class Meta:
        model = Host
        fields = ('name', 'address', 'mem_total', 'cpu_total', 'os_type', 'disk_total', 'group_name')

    def for_delete(self, row, instance):
        return self.fields['name'].clean(row) == ''


class HostAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = HostResource


# Register your models here.
# 进行注册到管理页面
admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup)
admin.site.register(user_profile)

