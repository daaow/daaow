from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def index(request):
    template = loader.get_template('score/index.html')
    return HttpResponse(template.render(ikk,request))
# Create your views here.
