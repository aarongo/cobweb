#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import xmlrpclib

ip_address = {
    "rest-api": {
        "rest-api-node1": "10.200.200.37",
        "rest-api-node2": "10.200.200.38",
        "rest-api-node3": "10.200.200.42",
        "rest-api-node4": "10.200.200.43"
    },
    "wap": {
        "wap-nginx": "10.200.200.76"
    }
}


def supervisorinfo():
    restful_list =[]
    number = 0
    for name in ip_address:
        for hostname in ip_address[name]:
            supervisor_url = 'http://user:123@%s:9001' % ip_address[name][hostname]
            server = xmlrpclib.Server(supervisor_url)
            process_name = server.supervisor.getAllProcessInfo()[0]['name']
            # print json.dumps(server.supervisor.getProcessInfo(process_name), indent=4)
            # restful = {hostname: server.supervisor.getProcessInfo(process_name)}
            restful_1 = server.supervisor.getProcessInfo(process_name)
            restful_1['hostname'] = hostname
            number += 1
            restful_list.append(restful_1)
    restful = {'code':0,'msg':'okm','data':restful_list,'count':number}
    return restful


def getdeatil(hostname):
    ip = ''
    for name in ip_address:
        for a in ip_address[name]:
            if hostname == a:
                ip = ip_address[name][a]
    supervisor_url = 'http://user:123@%s:9001' % ip
    server = xmlrpclib.Server(supervisor_url)
    process_name = server.supervisor.getAllProcessInfo()[0]['name']
    restful_1 = server.supervisor.getProcessInfo(process_name)
    return restful_1


def stopprocess(hostname):
    ip = ''
    for name in ip_address:
        for a in ip_address[name]:
            if hostname == a:
                ip = ip_address[name][a]
    supervisor_url = 'http://user:123@%s:9001' % ip
    server = xmlrpclib.Server(supervisor_url)
    process_name = server.supervisor.getAllProcessInfo()[0]['name']
    restful = server.supervisor.stopProcess(process_name)
    if restful:
        restful_1 = {'status': '停止成功'}
    return restful_1


def startprocess(hostname):
    ip = ''
    for name in ip_address:
        for a in ip_address[name]:
            if hostname == a:
                ip = ip_address[name][a]
    supervisor_url = 'http://user:123@%s:9001' % ip
    server = xmlrpclib.Server(supervisor_url)
    process_name = server.supervisor.getAllProcessInfo()[0]['name']
    restful = server.supervisor.startProcess(process_name)
    if restful:
        restful_1 = {'status': '启动成功'}
    return restful_1


def restartprocess(hostname):
    ip = ''
    for name in ip_address:
        for a in ip_address[name]:
            if hostname == a:
                ip = ip_address[name][a]
    supervisor_url = 'http://user:123@%s:9001' % ip
    server = xmlrpclib.Server(supervisor_url)
    process_name = server.supervisor.getAllProcessInfo()[0]['name']
    restful = server.supervisor.restart()
    if restful:
        restful_1 = {'status': '重启成功'}
    return restful_1