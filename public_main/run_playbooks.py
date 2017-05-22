#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import task
import os
import json


# 运行 playbooks
def playbooks_run(parameters):
    yaml_name = "s_cobweb/ansible_playbooks/" + "%s" % parameters['hosts'] + ".yml"
    yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', yaml_name))
    file_path_hosts = os.path.abspath(os.path.join(os.path.dirname(__file__), 'custom_auto_inventory.py'))
    code_run = task.MyRunner().run_playbooks(host_list=file_path_hosts, playbook_path=yaml_path, extra_vars=parameters)


# playbooks_run(parameters={'hosts': 'group1', 'roles': 'master', 'version': '3.0.0', 'Redis_Home': '/software/redis'})

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
        # 处理只有一个 task 的情况
        if len(resulttaskname()) != 1:
            # 处理一种当执行都成功时会出现result_1 中存放2次或者多次执行结果
            if value['ok'] == (len(resulttaskname())-1):
                # print key, "hahah"
                for index in range(0, len(resulttaskname())):
                    result_1.append(resulttaskname()[index])
                # 当执行多次是判断列表长度是否为当前的倍数,根据倍数进行裁剪 list 最后放入字典
                if len(result_1) == (len(resulttaskname()) * 2):
                    del result_1[0:(len(result_1)/2)]
                result[key] = result_1
            else:
                print key, "执行了%s" % value['ok']
                for index in range(0, len(resulttaskname())):
                    result_2.append(resulttaskname()[index])
                print result_2
                result[key] = result_2
        else:
            result[key] = [resulttaskname()[0]]
    return result



print resulttaskname()
print zdy_result()