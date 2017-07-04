# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	NetworkUser,
)


class NetworkUserCreateView(CreateView):

    model = NetworkUser


class NetworkUserDeleteView(DeleteView):

    model = NetworkUser


class NetworkUserDetailView(DetailView):

    model = NetworkUser


class NetworkUserUpdateView(UpdateView):

    model = NetworkUser


class NetworkUserListView(ListView):

    model = NetworkUser

