from django.conf.urls import url

from . import views

app_name = 'virtual_contest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createcontest/$', views.create_contest, name='create_contest'),
    url(r'^createcontest/add_problem/$', views.check_problem, name='check_problem'),
    url(r'^createcontest/add_user/$', views.check_user, name='check_user'),
    url(r'^contest/(?P<contest_id>[0-9]+)/$', views.contest, name='contest'),
]