from collections import OrderedDict
from django.shortcuts import render
from re import X, template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def timeline(request):
  snews = News.objects.all().order_by('-date_created')
  context = {}
  context['snews'] = snews

  template = loader.get_template('timeline.html')
  return HttpResponse(template.render(context, request)); HttpResponseRedirect((reverse('index')))

def galery(request):
  images = Image.objects.all().order_by('-date_created')
  context = {}
  context['images'] = images

  template = loader.get_template('galery.html')
  return HttpResponse(template.render(context, request)); HttpResponseRedirect(reverse('index'))

def whippets(request):
  whippets = Whippets.objects.all
  context = {}
  context['whippets'] = whippets

  template = loader.get_template('whippets.html')
  return HttpResponse(template.render(context, request)); HttpResponseRedirect(reverse('index.html')) 

def puppies(request):
  puppies = Puppies.objects.all().order_by('-date_of_birth')
  context = {}
  context['puppies'] = puppies

  template = loader.get_template('puppies.html')
  return HttpResponse(template.render(context, request)); HttpResponseRedirect(reverse('index.html'))


def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html'))
def links(request):
  template = loader.get_template('links.html')
  return HttpResponse(template.render()); HttpResponseRedirect(reverse('index.html'))

def headerView(request):
  template = loader.get_template('header.html')
  return HttpResponse(template.render())