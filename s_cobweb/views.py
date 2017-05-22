# _*_coding:utf-8_*_
# Create your views here.

import os, logging
from django.shortcuts import render
from public_main import insert_data, select_data, get_host_info, data_updata, run_playbooks
from django.contrib import auth
from wsgiref.util import FileWrapper
from django.http import HttpResponse, HttpResponseRedirect

# 用户注册
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from forms import RegisterForm


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
        return render(request, 'login.html')
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
            return render(request, 'login.html', {
                'login_status': 404
            })


@login_required
def author_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def index(request):
    return render(request, 'index.html')


def downloader(request):
    # test.tmp为将要被下载的文件名
    filename_tmp = 'systeminfo.xlsx'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(BASE_DIR, filename_tmp)
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename="systeminfo.xlsx"'
    return response


@login_required
def search(request):
    # 进行访问时首先刷新 json 文件
    data_updata.json_input()
    return render(request, 'search.html')


@login_required
def return_data(request):
    # 进行判断数据库是否更新过,如果更新过直接查询库填入 json 文件 如果没有 进行查询填入json 文件和更新数据库
    if data_updata.data_exist() != data_updata.count_host():
        ip = select_data.get_address()
        data_source = get_host_info.get_info(host=ip)
        data_updata.update_data(data=data_source)
        get_host_info.input_json(dictobj=data_source)
    else:
        data_updata.json_input()
        return HttpResponse("已经更新过了")
    return HttpResponse("更新数据")


@login_required
# 提交数据时的临时调用方法
def submit_tmp(request):
    return render(request, 'insert.html')


@login_required
# 提交数据真正调用的方法
def submit_data(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    else:
        address = request.POST.get('address')
        groupname = request.POST.get('group_name')
        g_status = insert_data.insert_group(groupname=groupname)
        h_status = insert_data.insert_host(address=address, group_name=groupname)
        return render(request, 'insert.html', {
            "g_status": g_status,
            "h_status": h_status,
        })




@login_required
# 安装软件临时 URL
def software_tmp(request):
    group = select_data.get_gorups()
    return render(request, 'software_install.html', {
        "groups": group,
        "action": dict(send_ssh_key="authorized", system_init="system_init", tomcat_install="tomcat",
                       nginx_install="nginx", mysql_install="mysql", memcached_install="memcached",
                       mongodb_install="mongodb_cluster", redis_install="redis", solrcloud="solrcloud",
                       zookeeper="zookeeper-cluster", zabbix_agent_install="zabbix_agent")
    })


@login_required
# 安装 运行的 yml 要与组名一致 在 run_playbooks中直接获取
def software_install(request):
    actionname = request.POST.get('action_name')
    groupname = request.POST.get('groupname')
    varname = request.POST.get('vars')
    print groupname, actionname, varname, type(eval(varname))
    logger = logging.getLogger('scripts')  # setting.py中配置的logger
    logger.info(run_playbooks.playbooks_run(parameters=eval(varname)))
    return render(request, 'software_install.html', {
        "run_status": run_playbooks.zdy_result(),
        "run_all_status": run_playbooks.resultall_status()
    })


def test(request):
    return render(request, 'index.html')


def inset(request):
    hostname = request.POST.get('hostname')
    ipaddress = request.POST.get('ipaddress')
    groupname = request.POST.get('groupname')
    insert_data.insert_host(name=hostname, address=ipaddress,groupname=groupname)
    return render(request, 'insetdata.html')