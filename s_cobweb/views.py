# _*_coding:utf-8_*_
# Create your views here.


import json


from django.contrib import auth
from django.contrib.auth import authenticate, login
# 用户注册
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from forms import RegisterForm
from public_main import mysql_handle, get_host_info, supervisor_info


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


def author_login(request):
    # 判断前端请求类型
    if request.method == 'GET':
        return render(request, 'login_v2.html')
    else:
        # 获取到 post 过来的数据
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 用 django  authenticate方法将前台的传过来的参数处理
        user = auth.authenticate(username=username, password=password)
        # 判断用户是否为空,和是不是存在 user表里是否有此用户
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            # 进行用户登录
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'login_v2.html', {
                'login_status': 404
            })


@login_required
def author_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def index(request):
    return render(request, 'index.html')


# 获取主机信息
@login_required
def assets_json(request):
    # 前端传入分页信息
    pagenum = int(request.GET.get('pageNumber'))
    pagesize = int(request.GET.get('pageSize'))
    # 留下一个伏笔 get_host_info.py refush_data 方法 根据返回值来确定取值
    data = get_host_info.refush_data(pagenum, pagesize)
    return HttpResponse(json.dumps(data), content_type="application/json")


# 资产页面
@login_required
def assets_info(request):
    # 进行访问时首先刷新 json 文件
    #data_updata.json_input()
    return render(request, 'search.html')


@login_required
# 新增数据页面
def add_data(request):
    ip_address = str(request.GET.get('ip_address'))
    group = request.GET.get('group')
    supervisor_exit = request.GET.get('supervisor')
    if not supervisor_exit:
        supervisor_exit = 0
    inset_data = mysql_handle.insert_host(ip_address, group, supervisor_exit)
    ip = mysql_handle.supervisor_address()
    print ip
    print inset_data
    return HttpResponse("sfasdf")


# @login_required
# def return_data(request):
#     # 进行判断数据库是否更新过,如果更新过直接查询库填入 json 文件 如果没有 进行查询填入json 文件和更新数据库
#     if data_updata.data_exist() != data_updata.count_host():
#         ip = mysql_handle.get_address()
#         data_source = get_host_info.get_info(host=ip)
#         data_updata.update_data(data=data_source)
#         get_host_info.input_json(dictobj=data_source)
#     else:
#         data_updata.json_input()
#         return HttpResponse("已经更新过了")
#     return HttpResponse("更新数据")


@login_required
def supervisor_json(request):
    return HttpResponse(json.dumps(supervisor_info.control().supervisor_information()), content_type="application/json")


@login_required
def process_info(request):
    return render(request, 'process_info.html')


@login_required
def information_detail(request):
    hostname = str(request.GET.get('f_hostname'))
    pid = int(request.GET.get('pid'))
    data = supervisor_info.control(hostname=hostname, pid=pid).supervisor_deatil()
    return render(request, 'getDetail.html', {
        'data': data
    })


@login_required
def process_stop(request, f_hostname):
    r_status = supervisor_info.control(hostname=f_hostname).process_stop()
    return HttpResponse(json.dumps(r_status), content_type="application/json")


@login_required
def process_start(request, f_hostname):
    r_status = supervisor_info.control(hostname=f_hostname).process_start()
    return HttpResponse(json.dumps(r_status), content_type="application/json")


@login_required
def process_restart(request, f_hostname):
    r_status = supervisor_info.control(hostname=f_hostname).process_restart()
    return HttpResponse(json.dumps(r_status), content_type="application/json")


