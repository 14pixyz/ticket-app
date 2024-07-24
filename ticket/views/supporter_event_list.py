from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-login')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-login')


class EventListView(BaseSupporterPermission, ListView):
    template_name = "supporter/event-list.html"