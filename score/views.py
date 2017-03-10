import pickle

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages

from .forms import LoginForm
from .utils import create_stu, info_to_json


def index(request):
    return render(request, 'score/home.html')

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
                score_pre = stu.get_score()
                score_pre['lessons'].sort(key=lambda x: x[1], reverse=True)
                request.session['score'] = score_pre
                request.session['login'] = True
                request.session['npass'] = stu.get_npass_lesson()
                request.session['elec'] = stu.get_elective() # 选修课

                messages.success(request, '登录成功')
                return render(request, 'score/index.html',
                              {'lessons':request.session.get('score').get('lessons'),
                               'npass': request.session.get('npass').get('nums')}
                              )
            else:
                messages.warning(request, login_info.get('info'))
                return render(request, 'score/login.html', {'form': form})
        else:
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})
    elif request.method == 'GET':
        if request.session.get('login') is True:
            lessons = request.session.get('score').get('lessons')
            tag = request.GET.get('tag', 'default')
            tags = {
                'npass': request.session.get('npass').get('npass'),
                'cet': list(filter(lambda x: '等级考试' in x, lessons)),
                'elec': request.session.get('elec').get('lessons'),
                'default':list(filter(lambda x: '等级考试' not in x, lessons))
            }
            return render(
                request,
                'score/index.html',
                {
                    'lessons': tags.get(tag, lessons),
                    'elec': tag == 'elec',
                    'cet': tag =='cet',
                }
            )
        else:
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})

def ulogout(request):
    request.session.flush()
    messages.success(request, "已登出")
    return HttpResponseRedirect('/')

def about(request):
    return render(request, 'score/about.html')
