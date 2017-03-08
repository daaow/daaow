import pickle

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from .forms import LoginForm
from .utils import create_stu, info_to_json


def index(request):
    context = {
        'text': "{}".format(
            request.session.get('info')
        )
    }
    return render(request, 'score/index.html', context)

def ulogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            stu = create_stu(
                form.cleaned_data['student_id'],
                form.cleaned_data['password']
            )
            login_info = stu.login()
            if login_info.get('status'):
                request.session['info'] = info_to_json(stu.get_info())
                request.session['score'] = stu.get_score()
                # TODO:
                # - score API 挂科记录接口待添加，暂时设置为False
                # - CET-4, CET-6 接口
                request.session['score']['npass'] = False
                request.session['login'] = True
                # request.session['elec'] = stu.elec # 选修课

                return render(request, 'score/index.html',
                              {'text': stu.get_info(),
                               'login': request.session.get('login')})
            else:
                context = {
                    'text': login_info.get('info'),
                }
                return HttpResponse(login_info.get('info'))
        else:
            # TODO:
            # - django 消息框架
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form, 'login': request.session.get('login')})
    elif request.method == 'GET':
        if request.session.get('login') is True:
            tag = request.GET.get('tag')
            if tag == 'npass':
                return render(
                    request,
                    'score/index.html',
                    {
                        'tag': 'npass'
                    }
                )
            else:
                return render(
                    request,
                    'score/index.html',
                    {
                        'tag': 'all'
                    }
                )
        # TODO:
        # - 从缓存系统获取session
        else:
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})

def ulogout(request):
    request.session.flush()
    return HttpResponseRedirect('/score/')
