from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from ..forms import CustomUserCreateForm, CustomUserUpdateForm

# パーミッション
class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('ticket:supporter-home')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-home')


class CustomUserListView(BaseSupporterPermission, ListView):
    template_name = 'supporter/customuser-list.html'
    model = CustomUser
    paginate_by = 5


class CustomUserCreateView(BaseSupporterPermission, CreateView):
    template_name = 'supporter/customuser-create.html'
    model = CustomUser
    form_class = CustomUserCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy('ticket:supporter-customuser-list')


class CustomUserDeleteView(BaseSupporterPermission, DeleteView):
    template_name = 'supporter/customuser-delete.html'
    model = CustomUser
    success_url = reverse_lazy('ticket:supporter-customuser-list')


class CustomUserUpdateView(BaseSupporterPermission, UpdateView):
    template_name = 'supporter/customuser-update.html'
    model = CustomUser
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy('ticket:supporter-customuser-list')