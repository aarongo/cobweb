# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 创建用户
class user_profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30, default='root')
    maintenance = "YW"
    Sales = "XS"
    Test = "CS"
    department_choices = (
        (maintenance, '运维部'),
        (Sales, '销售部'),
        (Test, '测试部'),
    )
    department = models.CharField(max_length=2, choices=department_choices, default=maintenance)
    description = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


# 创建主机组
class HostGroup(models.Model):
    name = models.CharField('主机组名称', max_length=100, primary_key=True)
    exist = models.IntegerField('status', default=0)

    def __unicode__(self):
        return self.name


# 创建主机表
class Host(models.Model):
    name = models.CharField('主机名', max_length=100, null=True, blank=True)
    address = models.GenericIPAddressField('ip地址', null=False, blank=False, primary_key=True)
    mem_total = models.IntegerField('内存', null=True, blank=True, default=0)
    cpu_total = models.IntegerField('cpu个数', null=True, blank=True, default=0)
    os_type = models.CharField('操作系统类型', max_length=220, null=True, blank=True, default='null')
    disk_total = models.IntegerField('硬盘总容量(GB)', null=True, blank=True, default=0)
    group_name = models.CharField('主机组名称', max_length=200, null=True, blank=True, default='null')
    exist = models.IntegerField('更新', default=0)
    supervisor_exist = models.IntegerField('是否存在supervisor', default=0)

    def __unicode__(self):
        return self.name



