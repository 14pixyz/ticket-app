from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from ticket.models import Event, Ticket, Reservation
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..forms import ReservationCreateForm


class ReservationCreateView(CreateView):
    template_name = 'customer/reservation-form.html'
    model = Reservation
    form_class = ReservationCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy('ticket:customer-event-list') #topページへ


class ReservationListView(ListView):
    template_name = "customer/reservation-list.html"
    model = Reservation
    paginate_by = 5

    # 現在のユーザーの情報を取得
    def get_queryset(self):
        customer = self.request.user.id
        return Reservation.objects.filter(customer=customer)
    # 上記で取得した情報でフィルタリングをかける
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation_list'] = self.get_queryset()  # フィルタリングされたクエリセットを取得
        return context