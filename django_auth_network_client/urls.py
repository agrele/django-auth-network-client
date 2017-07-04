# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^NetworkUser/~create/$",
        view=views.NetworkUserCreateView.as_view(),
        name='NetworkUser_create',
    ),
    url(
        regex="^NetworkUser/(?P<pk>\d+)/~delete/$",
        view=views.NetworkUserDeleteView.as_view(),
        name='NetworkUser_delete',
    ),
    url(
        regex="^NetworkUser/(?P<pk>\d+)/$",
        view=views.NetworkUserDetailView.as_view(),
        name='NetworkUser_detail',
    ),
    url(
        regex="^NetworkUser/(?P<pk>\d+)/~update/$",
        view=views.NetworkUserUpdateView.as_view(),
        name='NetworkUser_update',
    ),
    url(
        regex="^NetworkUser/$",
        view=views.NetworkUserListView.as_view(),
        name='NetworkUser_list',
    ),
	]
