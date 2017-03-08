from django.conf.urls import url

from . import views

app_name = 'score'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^score/$', views.ulogin, name='score'),
    url(r'^logout/$', views.ulogout, name='logout'),
]
