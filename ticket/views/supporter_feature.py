from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


# パーミッション
class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('ticket:supporter-login')

    raise_exception = False
    login_url = reverse_lazy('ticket:supporter-login')


# サポータートップ
class HomeView(BaseSupporterPermission, TemplateView):
    template_name = 'supporter/home.html'


# ログイン機能
class SupporterLoginView(LoginView):
    template_name = 'supporter/login.html'
    success_url = reverse_lazy('ticket:supporter-login')

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('ticket:supporter-home')
        else:
            return reverse_lazy('ticket:supporter-login')


# ログアウト機能
class SupporterLogoutView(LogoutView):
    template_name = 'supporter/logout.html'