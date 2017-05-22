#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

'''
使用此方法进行 mysql 数据的插入
'''

import LightMysql


# 初始化执行 sql 类
def mysql_runner():
    Runner = LightMysql.main()
    return Runner


# 查询组是否存在
def select_gorup():
    groupname_list = []
    sql = "SELECT name FROM s_cobweb_hostgroup;"
    result_select = mysql_runner().select(sql)
    for name in result_select:
        groupname_list.append(name['name'])
    return groupname_list


# 查询主机host
def select_host():
    hostip_list = []
    sql = "SELECT address FROM s_cobweb_host;"
    result_select = mysql_runner().select(sql)
    for ip in result_select:
        hostip_list.append(ip['address'])
    return hostip_list


# 插入组
def insert_group(groupname):
    if groupname in select_gorup():
        return 1
    else:
        sql = "INSERT INTO s_cobweb_hostgroup(name) VALUES ('%s')" % groupname
        result_insert_group = mysql_runner().dml(sql)
        return result_insert_group


# 插入主机
def insert_host(address, group_name):
    if address in select_host():
        return 1
    else:
        sql = "INSERT INTO s_cobweb_host(address, group_name) VALUES ('%s','%s')"%(address, group_name)
        result_insert_host = mysql_runner().dml(sql)
        return result_insert_host