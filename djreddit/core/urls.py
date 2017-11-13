from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^posts/(?P<pk>[0-9]+)$', views.PostDetailView.as_view(), name='posts.show'),
    url(r'^$', views.index_view, name='index'),
]
