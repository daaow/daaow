import pickle

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from .forms import LoginForm
from .utils import create_stu


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
                request.session['info'] = stu.get_info()
                request.session['score'] = stu.get_score()
                request.session['login'] = True
                # request.session['elec'] = stu.elec # 选修课

                return render(request, 'score/index.html',
                              {'text': stu.get_info()})
            else:
                context = {
                    'text': login_info.get('info')
                }
                return HttpResponse(login_info.get('info'))
        else:
            # TODO:
            # - django 消息框架
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})
    else:
        if request.session.get('login') is True:
            return render(
                request,
                'score/index.html',
                {
                    'text': request.session.get('info')
                })
        # TODO:
        # - 从缓存系统获取session
        else:
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})

# TODO:
# - 用户登出 requests.sesssion.flush()

def indexshow(request):
    context = {
        'text': "helloworld",
    }
    return render(request, 'score/index.html', context)

