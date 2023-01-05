from django.shortcuts import render
from re import X, template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def timeline(request):
  template = loader.get_template('timeline.html')
  return HttpResponse(template.render()); HttpResponseRedirect((reverse('index')))
def galery(request):
  template = loader.get_template('galery.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index'))
def whippets(request):
  template = loader.get_template('whippets.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html')) 
def puppies(request):
  template = loader.get_template('puppies.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html'))
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html'))
def contact(request):
  template = loader.get_template('links.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html'))

def headerView(request):
  template = loader.get_template('header.html')
  return HttpResponse(template.render())