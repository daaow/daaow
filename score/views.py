from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from .forms import LoginForm
from .utils import create_stu


def index(request):
    context = {
        'text': 'hello world'
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
            user = authenticate(
                username=form.cleaned_data['student_id'],
                password=form.cleaned_data['password']
            )

            login_info = stu.login()
            if login_info.get('status'):
                # login(request, user)
                return render(request, 'score/info.html',
                              {'text': stu.get_score()})
            else:
                context = {
                    'text': login_info.get('info')
                }
                return HttpResponse(login_info.get('info'))
        else:
            form = LoginForm()
            return render(request, 'score/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'score/login.html', {'form': form})

