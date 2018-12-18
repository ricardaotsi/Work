from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit\?cracha=(?P<cracha>\d+)&ativo=(?P<ativo>\D+)$', views.edit, name='edit'),
]