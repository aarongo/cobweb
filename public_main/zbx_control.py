#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import json
import urllib2
from urllib2 import *
import converbytes


class zbx_tools(object):
    def __init__(self):
        self.url = "http://10.200.200.75/api_jsonrpc.php"
        self.header = {"Content-Type": "application/json"}
        self.authID = self.user_login()

    # 获取登录ID
    def user_login(self):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "liuyulong",
                    "password": "Tczaflw@521"
                },
                "id": 0,
            }
        )
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "Auth Failed, Please Check Your Name And Password:", e.code
        else:
            response = json.loads(result.read())
            result.close()
            authID = response['result']
            return authID

    # 获取数据
    def get_data(self, data, hostip=""):
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
            return 0
        else:
            response = json.loads(result.read())
            result.close()
            return response

    # 获取主机组
    def get_groups(self):
        return_groups = {}
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    # 只获取主机组 id 和名字
                    "output": ["real_hosts", "name"],
                },
                "auth": self.authID,
                "id": 1,
            })
        res = self.get_data(data)
        if 'result' in res.keys():
            res_g = res['result']
            if (res_g != 0) or (len(res_g) != 0):
                # print "\033[32mNumber Of Group: %s\033[0m" % len(res_g)
                # for group in res_g:
                #     print "HostGroup_id:", group['groupid'], "\t" "HostGroupName:", group['name']
                for info in res_g:
                    return_groups[info['name']] = info['groupid']
        return return_groups

    # 根据组ID获取主机
    def get_grouphost(self):
        for key, value in self.get_groups().items():
            if key == 'syzm_pro':
                data = json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                            "output": ["hostid", "name", "status", "host"],
                            "groupids": value,
                        },
                        "auth": self.authID,
                        "id": 1,
                    })
                res = self.get_data(data)['result']
                return res

    # 获取主机监控项
    def get_hostitem(self):
        items_get = ['vfs.fs.size[/software,free]', 'system.cpu.load[percpu,avg1]', 'vm.memory.size[available]',
                     'system.cpu.util[,idle]']
        return_items = []
        return_items_ip = {}
        # 根据组ID获取主机方法
        for hostid in self.get_grouphost():
            for search_name in items_get:
                data = json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "method": "item.get",
                        "params": {
                            "output": ["itemids", "key_"],
                            "hostids": hostid['hostid'],
                            "search": {
                                "key_": search_name
                            },
                            "sortfield": "name"
                        },
                        "auth": self.authID,
                        "id": 1,
                    })
                res = self.get_data(data)['result']
                return_items.append(res)
            return_items_ip[hostid['name']] = return_items
            # 每次循环添加完毕后清空列表进入下一次
            return_items = []
        print return_items_ip
        return return_items_ip
            #
            # print return_items_ip

            #     return_items.append(res)
            #     return_items_ip[hostid['name']] = res
            #
            # print return_items_ip

        #     #print res
        #     return_items[hostid['name']] = res
        # # # 根据需求返回 itemid 和监控项值
        # for item in return_items:
        #     for info in return_items[item]:
        #         if info['key_'] in items_get:
        #             return_items_ip[info['itemid'].encode('UTF-8')] = info['key_'].encode('UTF-8')
        # print return_items_ip

    # 获取监控项数据
    def get_items_data(self, itemid):
        result_data = {}
        for host in itemid:
            for i in range(len(itemid[host])):
                if itemid[host][i][-1]['key_'] == 'system.cpu.util[,idle]' or itemid[host][i][-1]['key_'] == 'system.cpu.load[percpu,avg1]':
                    data = json.dumps(
                        {
                            "jsonrpc": "2.0",
                            "method": "history.get",
                            "params": {
                                "output": "extend",
                                "history": 0,
                                "itemids": itemid[host][i][-1]['itemid'],
                                "limit": 1
                            },
                            "auth": self.authID,
                            "id": 1,
                        })
                else:
                    data = json.dumps(
                        {
                            "jsonrpc": "2.0",
                            "method": "history.get",
                            "params": {
                                "output": "extend",
                                "history": 3,
                                "itemids": itemid[host][i][-1]['itemid'],
                                "limit": 1
                            },
                            "auth": self.authID,
                            "id": 1,
                        })
                res = self.get_data(data)['result']
                if (res != 0) and (len(res) != 0):
                    value = str(res[-1]['value'])
                    if float(value) > 1024:
                        size = converbytes.main(bytes=int(value))
                        result_data[itemid[host][i][-1]['key_']] = size
                        print "%s" % host, "%s" % itemid[host][i][-1]['key_'], size
                    else:
                        result_data[itemid[host][i][-1]['key_']] = size
                        print "%s" % host, "%s" % itemid[host][i][-1]['key_'], value

                print res
if __name__ == '__main__':
    a = zbx_tools()
    # a.get_host(hostip='dubbo-price_node1')
    # a.get_groups()
    # a.get_grouphost()
    # a.get_hostinterface(hostid='10106')
    a.get_items_data(itemid=a.get_hostitem())
    # a.get_grouphost()
    # a.get_hostitem()

