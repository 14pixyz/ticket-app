from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from ticket.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
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

    # 現在のユーザーの情報を取得
    def get_queryset(self):
        company = self.request.user.company_id
        return CustomUser.objects.filter(company=company)
    # 上記で取得した情報でフィルタリングをかける
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customuser_list'] = self.get_queryset()  # フィルタリングされたクエリセットを取得
        return context


class CustomUserCreateView(BaseSupporterPermission, CreateView):
    template_name = 'supporter/customuser-create.html'
    model = CustomUser
    form_class = CustomUserCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # CreateViewのget_form_kwargsを呼び出す
        kwargs['request'] = self.request  # リクエストオブジェクトをフォームに渡す
        return kwargs

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