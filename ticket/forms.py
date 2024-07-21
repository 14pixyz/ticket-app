from django import forms
from .models import CustomUser

class CustomUserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]
        labels = {
            'username': 'サポーター名',
            'email': 'メールアドレス',
        }
