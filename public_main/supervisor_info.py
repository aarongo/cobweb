#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import xmlrpclib


class control(object):
    ip_address = {
        "rest-api-node1": "10.200.200.37",
        "rest-api-node2": "10.200.200.38",
        "rest-api-node3": "10.200.200.42",
        "rest-api-node4": "10.200.200.43",
        "wap-nginx": "10.200.200.76",
        "syzmm_maintenance-node1": "10.200.200.45"
    }

    def __init__(self, hostname=None, pid=None, custom_result=None):
        # 所有的实例都共享此变量，即不单独为每个实例分配
        if custom_result is None:
            custom_result = {}
        # view 中方法获取前端传过来的主机名进行赋值,后续方法调用
        self.hostname = hostname
        # view 中方法获取前端传过来的pid进行赋值,后续方法调用
        self.pid = pid
        self.custom_result = custom_result

    # 根据前端传过来的主机名进行实例化连接 supervisorAPI
    def supervisor_base(self):
        supervisor_url = 'http://user:123@%s:9001' % control.ip_address[self.hostname]
        connect_server = xmlrpclib.Server(supervisor_url)
        return connect_server

    # 根据前端端和 ipaddress 变量进行程序名称的获取
    def handle_base(self):
        server = self.supervisor_base()
        process_name = server.supervisor.getAllProcessInfo()[0]['name']
        return process_name

    '''
    1. 获取进程所有信息---并且处理所需数据使用 dict(ipaddress)
    2. 将数据通过 view 方法返回给前端返回 json 数据
    '''
    def supervisor_information(self):
        result_list = []
        number = 0
        for hostname in control.ip_address:
            server = control(hostname=hostname).supervisor_base()
            supervisor_process_info = server.supervisor.getAllProcessInfo()
            if len(supervisor_process_info) > 1:
                for num in range(len(supervisor_process_info)):
                    process_name = supervisor_process_info[num]['name']
                    result_1 = server.supervisor.getProcessInfo(process_name)
                    result_1['hostname'] = hostname
                    result_1['ipaddress'] = control.ip_address[hostname]
                    number += 1
                    result_list.append(result_1)
            else:
                process_name = supervisor_process_info[0]['name']
                result_1 = server.supervisor.getProcessInfo(process_name)
                result_1['hostname'] = hostname
                result_1['ipaddress'] = control.ip_address[hostname]
                number += 1
                result_list.append(result_1)
        restful = {'code': 0, 'msg': 'okm', 'data': result_list, 'count': number}
        return restful

    # 根据前端传过来的主机名和 pid 进行唯一性校验,并获取该 主机名对应的 IP
    # f == front(前端)
    def supervisor_deatil(self):
        process = []
        data_source = {}
        server = control(hostname=self.hostname).supervisor_base()
        # 处理一台服务器上有多个进程时,前端页面进行查看时只显示一条
        if len(server.supervisor.getAllProcessInfo()) > 1:
            for num in range(len(server.supervisor.getAllProcessInfo())):
                process_name = server.supervisor.getAllProcessInfo()[num]['name']
                restful_1 = server.supervisor.getProcessInfo(process_name)
                process.append(restful_1)
        else:
            process_name = server.supervisor.getAllProcessInfo()[0]['name']
            restful_1 = server.supervisor.getProcessInfo(process_name)
            process.append(restful_1)
        # 处理单台服务器多个进程显示问题,以 PID 为唯一标识返回 dict
        for data in process:
            for key in data:
                if self.pid == data[key]:
                    data_source = data
        return data_source

    # view 方法传参hostname
    def process_stop(self):
        server = self.supervisor_base()
        result = server.supervisor.stopProcess(self.handle_base())
        if result:
            self.custom_result = {'status': '停止成功'}
        return self.custom_result

    # view 方法传参hostname
    def process_start(self):
        server = self.supervisor_base()
        result = server.supervisor.startProcess(self.handle_base())
        if result:
            self.custom_result = {'status': '启动成功'}
        return self.custom_result

    # view 方法传参hostname
    def process_restart(self):
        server = self.supervisor_base()
        if len(server.supervisor.getAllProcessInfo()) > 1:
            result = server.supervisor.signalProcess(self.handle_base(), 'HUP')
        else:
            result = server.supervisor.restart()
        if result:
            self.custom_result = {'status': '重启成功'}
        return self.custom_result





