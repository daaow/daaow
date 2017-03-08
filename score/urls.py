from django.conf.urls import url

from . import views

app_name = 'score'
urlpatterns = [
    url(r'^$', views.indexshow, name='index'),
    url(r'^login/$', views.ulogin, name='login'),
]
