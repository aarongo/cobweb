#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import websocket
import time
import subprocess
import json


a = 1

while a == 1:
    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8000")
    ws.send("Hello World")
    time.sleep(1)

#
# def tomcat_log():
#     ws = websocket.WebSocket()
#     ws.connect("ws://localhost:8000")
#     command_tomcat_log = "ssh root@172.31.0.253 tail -f /install/nginx/logs/172.31.0.253_access.log "
#     p = subprocess.Popen(command_tomcat_log, shell=True,
#                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     returncode = p.poll()
#     try:
#         while returncode is None:
#             line = p.stdout.readline().strip()
#             print line
#             if line:
#                 ws.send(line)
#                 time.sleep(1)
#     except KeyboardInterrupt:
#         print 'ctrl+d or z'
#
# tomcat_log()