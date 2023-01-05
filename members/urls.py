from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/', views.timeline, name='timeline'),
    path('galery/', views.galery, name='galery'),
    path('whippets/', views.whippets, name='whippets'),
    path('puppies/', views.puppies, name='puppies'),
    path('contact/', views.contact, name='contact')
]