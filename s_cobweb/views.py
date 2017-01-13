# _*_coding:utf-8_*_
from django.shortcuts import render

# Create your views here.

import os
from django.shortcuts import render
from ansible_api import ansible_collect
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        # 获取到 post 过来的数据
        hostlist = request.POST.get('ipinput', '')
    hostlist = hostlist.split(',')
    ansible_collect.main(host_list=hostlist)

    return render(request, 'download.html', {
                'status': 200
            })


def downloader(request):
    # test.tmp为将要被下载的文件名
    filename_tmp = 'systeminfo.xlsx'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(BASE_DIR,filename_tmp)
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="systeminfo.xlsx"'
    return response