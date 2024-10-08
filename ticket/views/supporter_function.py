from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from ..forms import SignUpForm
from django.contrib.auth import authenticate, login


# パーミッション
class BaseSupporterPermission(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return user.is_staff or user.is_supporter
        return False

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

    def get_success_url(self):
        if self.request.user.is_staff or self.request.user.is_supporter:
            return reverse_lazy('ticket:supporter-home')
        else:
            return reverse_lazy('ticket:supporter-login')


# ログアウト機能
class SupporterLogoutView(LogoutView):
    template_name = 'supporter/logout.html'


# signup機能
def signup(request):
    signup_form = SignUpForm(request.POST or None)
    if signup_form.is_valid():
        try:
            user = signup_form.save()
            # ユーザー認証を行い、ログインさせる
            authenticated_user = authenticate(email=user.email, password=request.POST['password'])  # emailを使用して認証
            if authenticated_user is not None:
                login(request, authenticated_user)
            return redirect('ticket:supporter-home')
        except ValidationError as e:
            signup_form.add_error('password', e)
    return render(request, 'supporter/signup.html', context={
        'form': signup_form,
    })