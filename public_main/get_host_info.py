#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


from task import MyRunner
import json
import mysql_handle


# 获取 ansible setup 信息
def get_info(host):
    get_resluts = MyRunner().Order_Run(host_list=host,
                                       module_name='setup', module_args='')

    results_tamp = {}
    # result_list = []
    data = json.loads(get_resluts)
    # 根据出入的 iP 进行结果保存
    for ip in host:
        get_results = data['success'][ip]['ansible_facts']
        mem_total = get_results['ansible_memtotal_mb']
        # swap_total = get_results['ansible_swaptotal_mb']
        # cpu_type = get_results['ansible_processor'][-1].encode('utf-8')
        cpu_total = get_results['ansible_processor_vcpus']
        os_type = "".join((get_results['ansible_distribution'], get_results[
            'ansible_distribution_version'])).encode('utf-8')
        disk_total = sum([int(get_results["ansible_devices"][i]["sectors"]) *
                          int(get_results["ansible_devices"][i][
                                  "sectorsize"]) / 1024 / 1024 / 1024
                          for i in get_results["ansible_devices"] if i[0:2] in ("vd", "vs")])
        # server_type = get_results["ansible_product_name"].encode('utf-8')
        host_name = get_results["ansible_hostname"].encode('utf-8')
        # os_kernel = get_results["ansible_kernel"].encode('utf-8')
        results_tamp[ip] = {"ip": ip, 'mem_total': mem_total, 'cpu_total': cpu_total, 'os_type': os_type, 'disk_total': disk_total,'host_name': host_name}
        # result_list.append(results_tamp)
    # results = {'code': 0, 'msg': 'okm', 'rows': result_list, 'total': count}
    return results_tamp


# 是否更新过数据--返回一个状态 view 里判断状态进行下一步操作(其实无论什么状态都是从数据库拿数据)
def refush_data(pagenum, pagesize):
    if mysql_handle.data_exist() != mysql_handle.count_address():
        ip = mysql_handle.all_address()
        data_sour = get_info(host=ip)
        mysql_handle.update_data(data_sour)
        data = mysql_handle.get_address(pagenum, pagesize)
        return data
    else:
        data = mysql_handle.get_address(pagenum, pagesize)
        return data

# def search_data(term):
