from django import forms
from .models import CustomUser, Event
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
        user.is_supporter = True  # is_supporter を True に設定
        if commit:
            user = CustomUser.objects.create_user(
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password'],
                username=self.cleaned_data['username'],
                is_supporter=True
            )
        return user


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]
        labels = {
            'username': 'サポーター名',
            'email': 'メールアドレス',
        }


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "place", "adress", "max_seat", "date", "opening_time", "closing_time", "image", "web_site", "overview", "company"]
        labels = {
            'title': 'イベントタイトル',
            'place': '会場名',
            'adress': '住所',
            'max_seat': '座席数',
            'date': '公演日',
            'opening_time': '開始時間',
            'closing_time': '終了時間',
            'image': '画像',
            'web_site': 'webサイトURL',
            'overview': '概要',
            'image': '画像',
            'company': '団体情報',
        }


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "place", "adress", "max_seat", "date", "opening_time", "closing_time", "image", "web_site", "overview", "company"]
        labels = {
            'title': 'イベントタイトル',
            'place': '会場名',
            'adress': '住所',
            'max_seat': '座席数',
            'date': '公演日',
            'opening_time': '開始時間',
            'closing_time': '終了時間',
            'image': '画像',
            'web_site': 'webサイトURL',
            'overview': '概要',
            'image': '画像',
            'company': '団体情報',
        }