from django.shortcuts import render
from re import X, template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def galery(request):
  template = loader.get_template('galery.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index'))


def headerView(request):
  template = loader.get_template('header.html')
  return HttpResponse(template.render())