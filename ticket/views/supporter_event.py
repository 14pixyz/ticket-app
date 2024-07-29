from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import Event
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import EventCreateForm, EventUpdateForm


class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_supporter

    def handle_no_permission(self):
        return redirect('ticket:supporter-login')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-login')


class EventListView(BaseSupporterPermission, ListView):
    template_name = "supporter/event-list.html"
    model = Event
    paginate_by = 5

    # 現在のユーザーの情報を取得
    def get_queryset(self):
        company = self.request.user.company_id
        return Event.objects.filter(company=company)
    # 上記で取得した情報でフィルタリングをかける
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_list'] = self.get_queryset()  # フィルタリングされたクエリセットを取得
        return context

class EventCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/event-create.html'
    model = Event
    form_class = EventCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # CreateViewのget_form_kwargsを呼び出す
        kwargs['request'] = self.request  # リクエストオブジェクトをフォームに渡す
        return kwargs

    def get_success_url(self) -> str:
        return reverse_lazy('ticket:supporter-event-list')


class EventDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/event-delete.html'
    model = Event
    success_url = reverse_lazy('ticket:supporter-event-list')


class EventUpdateView(BaseSupporterPermission, UpdateView):
    template_name = 'supporter/event-update.html'
    model = Event
    form_class = EventUpdateForm
    success_url = reverse_lazy('ticket:supporter-event-list')