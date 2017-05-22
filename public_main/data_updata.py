#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

import LightMysql
import json
import os


# 初始化数据库连接
def mysql_runner():
    Runner = LightMysql.main()
    return Runner


# 更新数据库
def update_data(data):

    sql = "SELECT address from s_cobweb_host"
    result_addresss = mysql_runner().select(sql)
    # 当数据库ip 与 getinfo 出来的IP 相等时跟新此条数据
    for dict in result_addresss:
        for key in data:
            if dict['address'].encode('utf8') == key:
                sql = "UPDATE s_cobweb_host SET name='%s', cpu_total='%s', cpu_type='%s', " \
                      "disk_total='%s', mem_total='%s', os_kernel='%s', os_type='%s', " \
                      "server_type='%s',swap_total='%s', exist=1 WHERE address='%s'" \
                      % (data[key]['host_name'], data[key]['cpu_total'],
                         data[key]['cpu_type'], data[key]['disk_total'],
                         data[key]['mem_total'], data[key]['os_kernel'],
                         data[key]['os_type'], data[key]['server_type'],
                         data[key]['swap_total'], dict['address'].encode('utf8'))
                result_update = mysql_runner().dml(sql)
                if result_update == True:
                    print "数据库host表%s更新成功"%dict['address'].encode('utf8')
                else:
                    print "数据库host表%s更新失败" % dict['address'].encode('utf8')


def count_host():
    # 查询主机条数
    count_host = "SELECT * from s_cobweb_host"
    result_count = mysql_runner().select(count_host, 'count')
    return result_count


# 执行判断否更新
def data_exist():
    result = 0
    # 查询数据是否存在
    data_exist = "SELECT t.exist FROM s_cobweb_host t;"
    result_exist = mysql_runner().select(data_exist)
    for value in result_exist:
        result += value['exist']
    return result


# 查询数据库写入 data.json 文件
def json_input():
    sql = "SELECT * FROM s_cobweb_host"
    result = mysql_runner().select(sql)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static/json/data.json'))
    # 将列表些人文件
    thefile = open(file_path, 'w')

    json.dump(result, thefile)
    thefile.close()
