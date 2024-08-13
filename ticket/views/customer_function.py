from django.shortcuts import render, redirect, get_object_or_404
from ticket.models import Customer, Reservation
from ..forms import CustomerQueryForm

def query_view(request):
    if request.method == 'POST':
        form = CustomerQueryForm(request.POST)
        if form.is_valid():
            # フォームからデータを取得
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # 顧客データを照会
            try:
                customer = Customer.objects.get(username=username, email=email)
                # その顧客に関連する予約を取得
                reservation = Reservation.objects.filter(customer=customer).first()
                if reservation:
                    # 照会結果ページへリダイレクトし、クエリの結果を渡す
                    return redirect('ticket:customer-reservation-list', customer_id=customer.id, reservation_id=reservation.id)
                else:
                    form.add_error(None, '該当する予約がありません。')
            except Customer.DoesNotExist:
                form.add_error(None, 'ユーザー名またはメールアドレスが正しくありません。')
    else:
        form = CustomerQueryForm()
    return render(request, 'customer/query.html', {'form': form})