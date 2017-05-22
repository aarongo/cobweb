#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu

import argparse
import get_json_data


try:
    import json
except ImportError:
    import simplejson as json

mockData = get_json_data.selet_group_host()


def getList():
    '''get list hosts group'''
    print json.dumps(mockData)


def getVars(host):
    '''Get variables about a specific host'''
    print json.dumps(mockData[host]["vars"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', dest='list', help='get all hosts')
    parser.add_argument('--host', action='store', dest='host', help='get all hosts')
    args = parser.parse_args()

    if args.list:
        getList()

    if args.host:
        getVars(args.host)
