from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from ticket.models import Event, Ticket, Reservation
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import ReservationCreateForm


class ReservationCreateView(CreateView):
    template_name = 'customer/reservation-form.html'
    model = Reservation
    form_class = ReservationCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy('ticket:customer-event-list') #topページへ