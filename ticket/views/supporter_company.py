from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import CustomUserCreateForm, CustomUserUpdateForm

# パーミッション共通（改善の余地あり 2024-07-24 18:54:45）
class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-login')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-login')


class CustomUserListView(BaseSupporterPermission, ListView):
    template_name = 'supporter/customuser-list.html'
    model = CustomUser
    paginate_by = 5


class CustomUserCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/customuser-create.html'
    model = CustomUser
    form_class = CustomUserCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy('ticket:supporter-customuser-list')


class CustomUserDeleteView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')

    template_name = 'supporter/customuser-delete.html'
    model = CustomUser
    success_url = reverse_lazy('ticket:supporter-customuser-list')


class CustomUserUpdateView(BaseSupporterPermission, UpdateView):
    template_name = 'supporter/customuser-update.html'
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('ticket:supporter-customuser-list')