from django import forms
from .models import CustomUser, Event, Company, Ticket

class CustomUserCreateForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        labels = {
            'username': 'サポーター名',
            'email': 'メールアドレス',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)  # 親クラスの__init__メソッドを呼び出して、フォームの初期化処理を行う

    # フォーム保存時の動作
    def save(self):
        company_id = self.request.user.company_id  # リクエストオブジェクトからデータを取得
        user = super().save(commit=False)
        user = CustomUser.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            username=self.cleaned_data['username'],
            is_supporter=True,
            company=Company.objects.get(id=company_id),
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
        fields = ["title", "place", "adress", "max_seat", "date", "opening_time", "closing_time", "image", "web_site", "overview"]
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
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)  # 親クラスの__init__メソッドを呼び出して、フォームの初期化処理を行う

    # フォーム保存時の動作
    def save(self):
        event = super().save(commit=False)
        company_id = self.request.user.company_id  # リクエストオブジェクトからデータを取得
        event.company = Company.objects.get(id=company_id)
        event.save()
        return event



class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "place", "adress", "max_seat", "date", "opening_time", "closing_time", "image", "web_site", "overview"]
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
        }


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "price", "type", "area", "seat_number"]
        labels = {
            'title': 'チケット名',
            'price': '会場名',
            'type': '種別',
            'area': 'エリア',
            'seat_number': '座席番号',
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)  # 親クラスの__init__メソッドを呼び出して、フォームの初期化処理を行う

    # フォーム保存時の動作
    def save(self):
        ticket = super().save(commit=False)
        company_id = self.request.user.company_id  # リクエストオブジェクトからデータを取得
        ticket.company = Company.objects.get(id=company_id)
        ticket.save()
        return ticket



class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "price", "type", "area", "seat_number"]
        labels = {
            'title': 'チケット名',
            'price': '会場名',
            'type': '種別',
            'area': 'エリア',
            'seat_number': '座席番号',
        }



class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    company_name = forms.CharField(label="会社名", max_length=150)
    company_address = forms.CharField(label="会社住所", max_length=150)
    company_tel = forms.CharField(label="会社連絡先", max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        labels = {
            'username':'ユーザー名',
            'email':'メールアドレス',
            'password':'パスワード',
        }

    def save(self):
        # company情報をフォーム入力情報で作成する
        company_name = self.cleaned_data.get('company_name')
        company_address = self.cleaned_data.get('company_address')
        company_tel = self.cleaned_data.get('company_tel')
        company = Company.objects.create(name=company_name, adress=company_address, tel=company_tel)

        # 作成した情報からcompany_idを取得して、userデータに保存する
        user = super().save(commit=False)
        user.company = company
        user.is_staff = True
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

