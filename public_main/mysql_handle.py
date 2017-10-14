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
def select_data(sql):
    # sql = "SELECT * from s_cobweb_host"
    result_all = mysql_runner().select(sql)
    return result_all


# 执行判断否更新
def data_exist():
    result = 0
    # 查询数据是否存在
    data_exist = "SELECT t.exist FROM s_cobweb_host t;"
    result_exist = mysql_runner().select(data_exist)
    for value in result_exist:
        result += value['exist']
    return result


# 更新数据库
def update_data(data):

    sql = "SELECT address from s_cobweb_host"
    result_addresss = mysql_runner().select(sql)
    # 当数据库ip 与 getinfo 出来的IP 相等时跟新此条数据
    for dict in result_addresss:
        for key in data:
            if dict['address'].encode('utf8') == key:
                sql = "UPDATE s_cobweb_host SET name='%s', cpu_total='%s',disk_total='%s', mem_total='%s', os_type='%s', exist=1 WHERE address='%s'" \
                      % (data[key]['host_name'], data[key]['cpu_total'], data[key]['disk_total'], data[key]['mem_total'],
                         data[key]['os_type'], dict['address'].encode('utf8'))
                result_update = mysql_runner().dml(sql)
                if result_update == True:
                    print "数据库host表%s更新成功"%dict['address'].encode('utf8')
                else:
                    print "数据库host表%s更新失败" % dict['address'].encode('utf8')


# 获取IP地址=总条数=做分页使用
def count_address():
    sql = "SELECT * from s_cobweb_host"
    result_count = mysql_runner().select(sql, 'count')
    return int(result_count)


# 获取所有 IP 地址 提供第一次写入数据使用
def all_address():
    address = []
    sql = "SELECT address from s_cobweb_host"
    result_address = mysql_runner().select(sql)
    for ip in result_address:
        address.append(ip['address'].encode('utf8'))
    return address


# 获取IP地址-并且进行分页-并且直接返回数据
def get_address(num, size):
    pagesize = size
    pagenum = (num-1)*pagesize
    sql = "SELECT * from s_cobweb_host limit %s,%s" % (pagenum, pagesize)
    _result = mysql_runner().select(sql)
    results = {'code': 0, 'msg': 'okm', 'rows': _result, 'total': count_address()}
    return results


# 查询组
def get_gorups():
    group = []
    sql = "SELECT g.name FROM s_cobweb_hostgroup g"
    result_groups = mysql_runner().select(sql)
    for i in result_groups:
        group.append(i['name'].encode('utf8'))
    return group

if __name__ == '__main__':
    get_address(num=1,size=10)