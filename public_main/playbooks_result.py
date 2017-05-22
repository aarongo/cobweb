#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

import json
import LightMysql


# 初始化数据库连接
def mysql_runner():
    Runner = LightMysql.main()
    return Runner


# 获取IP地址
def get_address():
    address = []
    sql = "SELECT address from s_cobweb_host"
    result_address = mysql_runner().select(sql)
    for ip in result_address:
        address.append(ip['address'].encode('utf8'))
    return address


# 读取运行完 playbook 后生成的 Json 文件
def read_json():
    json_path = "/Users/lonny/Documents/cobweb/static/json/ansible_callback_json.json"
    with open(json_path) as data_file:
        data = json.load(data_file)
    return data


# 直接返回整体运行结果状态
def resultall_status():
    return read_json()['stats']


# 返回执行过程中的 task id 和 name
def resulttaskname():
    tasks_list = read_json()['plays'][-1]['tasks']
    result_tasks = {}
    for index, value in enumerate(tasks_list):
        result_tasks[index] = tasks_list[index]['task']
    return result_tasks


# 对比执行结果 根据主机记录没有执行成功的 tasks name
def zdy_result():
    result = {}
    result_1 = []
    result_2 = []
    for key, value in resultall_status().items():
        if value['ok'] == (len(resulttaskname())-1):
            # print key, "hahah"
            for index in range(1, value['ok']):
                result_1.append(resulttaskname()[index])
            result[key] = result_1
        else:
            # print key, "执行了%s" % value['ok']
            for index in range(1, value['ok']):
                result_2.append(resulttaskname()[index])
            result[key] = result_2
    return result
print zdy_result()

