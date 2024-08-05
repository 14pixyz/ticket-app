from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from ticket.models import Event, Ticket
from django.urls import reverse_lazy
from django.shortcuts import redirect


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


class EventDetailView(DetailView):
    template_name = 'customer/event-detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_list'] = Ticket.objects.filter(event__id=self.kwargs['pk'])
        return context