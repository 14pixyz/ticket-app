from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import Ticket
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import TicketCreateForm, TicketUpdateForm



class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_supporter

    def handle_no_permission(self):
        return redirect('ticket:supporter-login')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-login')


class TicketListView(BaseSupporterPermission, ListView):
    template_name = "supporter/ticket-list.html"
    model = Ticket
    paginate_by = 5

    # 現在のユーザーの情報を取得
    def get_queryset(self):
        company = self.request.user.company_id
        return Ticket.objects.filter(company=company)
    # 上記で取得した情報でフィルタリングをかける
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket_list'] = self.get_queryset()  # フィルタリングされたクエリセットを取得
        return context


class TicketCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/ticket-create.html'
    model = Ticket
    form_class = TicketCreateForm

    def get_success_url(self) -> str:
        event_id = self.request.POST.get('event')
        return reverse_lazy('ticket:supporter-event-detail', kwargs={'pk':int(event_id)})


class TicketDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/ticket-delete.html'
    model = Ticket

    def get_success_url(self) -> str:
        event_id = self.request.POST.get('event')
        return reverse_lazy('ticket:supporter-event-detail', kwargs={'pk':int(event_id)})


class TicketUpdateView(BaseSupporterPermission, UpdateView):
    template_name = 'supporter/ticket-update.html'
    model = Ticket
    form_class = TicketUpdateForm

    def get_success_url(self) -> str:
        event_id = self.request.POST.get('event')
        return reverse_lazy('ticket:supporter-event-detail', kwargs={'pk':int(event_id)})