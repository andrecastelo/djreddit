from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^$', views.index_view, name='index'),
]
