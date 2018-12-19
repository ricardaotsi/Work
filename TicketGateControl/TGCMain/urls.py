from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('edit/',views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    #url(r'^insert/$', views.insert, name='insert'),
    #url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit\?cracha=(?P<cracha>\d+)&matricula=(?P<matricula>\d+)&ativo=(?P<ativo>\D+)$', views.edit, name='edit'),
]