<コマンド集>
python manage.py makemigrations

python manage.py createsuperuser
python manage.py runserver
pip install -r requirements.txt
git branch -d <ブランチ名>


<説明>
・create superuserコマンドで、superuserを作成する
・イベントを作成したい代表ユーザーはallauthによって、sign up　を行い登録する
・代表ユーザーは　is_staff　である
・代表ユーザーはサポーター管理によって、サポートユーザー（is_supporter）を追加することができる
・代表ユーザーはサポーターの追加・編集・削除ができる
・代表ユーザーはイベントの追加・編集・削除ができる

・サポートユーザーはイベントの編集ができる
・サポートユーザーはイベントの編集ができる

<memo>
compnay.idにて特定のユーザーしかアクセスできないようにする
event.idにてイベントと紐づけて、イベントで混ざらないように管理する

event画面でevent.idを取得する → 値をforms.pyへ渡す　→ チケット作成画面でevent.idを保存する
