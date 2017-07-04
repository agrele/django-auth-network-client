# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_auth_network_client.urls import urlpatterns as django_auth_network_client_urls

urlpatterns = [
    url(r'^', include(django_auth_network_client_urls, namespace='django_auth_network_client')),
]
