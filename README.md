<コマンド集>
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
pip install -r requirements.txt
git branch -d <ブランチ名>


<説明>
・create superuserコマンドで、superuserを作成する
・イベントを作成したい代表ユーザーはallauthによって、sign up　を行い登録する
・代表ユーザーはサポーター管理によって、サポートユーザーを追加することができる
・サポートユーザーはイベントの編集ができる


・superuserのみcustomuserを追加できる