#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

import LightMysql
import json


# 初始化执行 sql 类
def mysql_runner():
    Runner = LightMysql.main()
    return Runner


# 获取组
def select_group():
    group_list = []
    sql = "SELECT name FROM s_cobweb_hostgroup;"
    result = mysql_runner().select(sql)
    for i in result:
        group_list.append(i['name'].encode('utf-8'))
    return group_list


def selet_group_host(group_list=select_group()):
    # 定义最外层字典(以主机组为key)
    whj = {}
    # 根据主机组循环组内主机
    for i in group_list:
        sql = "SELECT h.address FROM s_cobweb_hostgroup g, s_cobweb_host h  " \
              "WHERE g.name = h.group_name AND g.name = '%s'"% i
        result = mysql_runner().select(sql)
        # 定义循环出来的 ip 存放 list
        host_list = []
        # host_dict = {}
        # 将 ip 添加到 list 中
        for a in result:
            # host_dict = {"hosts": a['address'], "vars": {
            #     'ansible_ssh_port': 22,
            #     'ansible_ssh_user': "root",
            # }}
            host_list.append(a["address"].encode('utf-8'))
        # 添加到以主机组为key的主机集合
        whj[i] = {"hosts": host_list, "vars": {
            'ansible_ssh_port': 22,
            'ansible_ssh_user': "root",
        }}
    # 处理结果为分级 json
    #return json.dumps(whj, indent=4)
    return whj
