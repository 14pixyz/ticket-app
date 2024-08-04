from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from ticket.models import Event, Ticket
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import EventCreateForm, EventUpdateForm


class EventListView(ListView):
    template_name = "customer/event-list.html"
    model = Event
    paginate_by = 5

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET
        # フィルタリング
        if event_title := query.get('event_title'):
            queryset = queryset.filter(title__icontains=event_title).order_by('id')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_title'] = self.request.GET.get('event_title', '')
        return context