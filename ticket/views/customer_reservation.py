from django.views.generic import ListView, CreateView
from ticket.models import Reservation
from django.urls import reverse_lazy, reverse
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

    def get(self, request, *args, **kwargs):
        referer = request.META.get('HTTP_REFERER')
        # リファラURLを指定
        expected_referer = reverse('ticket:customer-query')
        # リファラURLを含まない場合はリダイレクト
        if not referer or expected_referer not in referer:
            return redirect('ticket:customer-event-list')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')  # URLパラメータからcustomer_idを取得
        reservation_id = self.kwargs.get('reservation_id')  # URLパラメータからreservation_idを取得
        queryset = Reservation.objects.filter(customer_id=customer_id)
        # 特定の予約IDでフィルタリング
        if reservation_id:
            queryset = queryset.filter(id=reservation_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation_list'] = self.get_queryset()  # フィルタリングされたクエリセットを取得
        return context