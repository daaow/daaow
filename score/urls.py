from django.conf.urls import url

from . import views

app_name = 'score'
urlpatterns = [
    url(r'^$', views.indexshow, name='indexshow'),
    url(r'^login/$', views.ulogin, name='login'),
]
