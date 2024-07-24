from django import forms
from .models import CustomUser
from django.shortcuts import redirect

class CustomUserCreateForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='パスワード（確認）', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password_confirm"]
        labels = {
            'username': 'サポーター名',
            'email': 'メールアドレス',
        }

    # パスワード確認のバリデーション
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("パスワードが一致しません。")

    # フォーム保存時の動作
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # is_staff を True に設定
        if commit:
            user = CustomUser.objects.create_user(
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],
                username=self.cleaned_data['username'],
                is_staff=True
            )
        return user



# 着手中　2024/07/24
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]
        labels = {
            'username': 'サポーター名',
            'email': 'メールアドレス',
        }