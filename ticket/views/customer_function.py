from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from ..forms import SignUpForm

# ログイン機能
class CustomerLoginView(LoginView):
    template_name = 'customer/login.html'
    success_url = reverse_lazy('ticket:customer-reservation-list')

    def get_success_url(self):
        if self.request.user.is_staff or self.request.user.is_supporter:
            return reverse_lazy('ticket:supporter-home')
        else:
            return reverse_lazy('ticket:supporter-login')