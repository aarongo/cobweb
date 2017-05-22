#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu
'''
提供查询数据使用
'''


import LightMysql


# 初始化数据库连接
def mysql_runner():
    Runner = LightMysql.main()
    return Runner


# 查询数据库
def select_data():
    sql = "SELECT * from s_cobweb_host"
    result_all = mysql_runner().select(sql)
    return result_all


# 统计主机
def host_numbers():
    sql = "SELECT * from s_cobweb_host"
    # 统计条数--即统计主机
    result_count = mysql_runner().select(sql, 'count')
    return result_count


# 获取IP地址
def get_address():
    address = []
    sql = "SELECT address from s_cobweb_host"
    result_address = mysql_runner().select(sql)
    for ip in result_address:
        address.append(ip['address'].encode('utf8'))
    return address


# 查询组
def get_gorups():
    group = []
    sql = "SELECT g.name FROM s_cobweb_hostgroup g"
    result_groups = mysql_runner().select(sql)
    for i in result_groups:
        group.append(i['name'].encode('utf8'))
    return group