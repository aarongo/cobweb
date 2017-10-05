#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


from task import MyRunner
import json
import os


# 获取 ansible setup 信息
def get_info(host):
    get_resluts = MyRunner().Order_Run(host_list=host,
                                       module_name='setup', module_args='')

    resluts = {}

    data = json.loads(get_resluts)
    print data
    # 根据出入的 iP 进行结果保存
    for ip in host:
        get_results = data['success'][ip]['ansible_facts']
        mem_total = get_results['ansible_memtotal_mb']
        swap_total = get_results['ansible_swaptotal_mb']
        cpu_type = get_results['ansible_processor'][-1].encode('utf-8')
        cpu_total = get_results['ansible_processor_vcpus']
        os_type = "".join((get_results['ansible_distribution'], get_results[
            'ansible_distribution_version'])).encode('utf-8')
        disk_total = sum([int(get_results["ansible_devices"][i]["sectors"]) *
                          int(get_results["ansible_devices"][i][
                                  "sectorsize"]) / 1024 / 1024 / 1024
                          for i in get_results["ansible_devices"] if i[0:2] in ("vd", "vs")])
        server_type = get_results["ansible_product_name"].encode('utf-8')
        host_name = get_results["ansible_hostname"].encode('utf-8')
        os_kernel = get_results["ansible_kernel"].encode('utf-8')
        resluts[ip] = {"ip": ip, 'mem_total': mem_total,
                       'swap_total': swap_total, 'cpu_type': cpu_type,
                       'cpu_total': cpu_total, 'os_type': os_type,
                       'disk_total': disk_total, 'server_type': server_type,
                       'host_name': host_name, 'os_kernel': os_kernel}
    return resluts


# 获取数据添加到 data.json 文件--直接获取执行结果给 data.json
def input_json(dictobj):
    list_data = []
    for value in dictobj.values():
        print value
        list_data.append(value)
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static/json/data.json'))
    # 将列表些人文件
    thefile = open(file_path, 'w')

    json.dump(list_data, thefile)
    thefile.close()