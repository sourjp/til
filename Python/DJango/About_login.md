

## loginの基本形
authenticate()を利用することでUser objectから存在を確認する  
login() login cookieを作成する

https://docs.djangoproject.com/ja/3.0/topics/auth/default/

```Views.py
from django.contrib.auth import authenticate, login

def my_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
    return render(xxx)
```

ちなみにreturnはrenderでもいいし、return redirect('namespace') でもいい

logoutの場合は logout(request) とすれば良い

## @login_required
from django.contrib.auth.decorators import login_required

を利用してviewsでdecoratorで使うと楽チン
要はis_authenticatedかどうかを評価する
notの時はredirect先としてsettings.pyのLOGIN_URLを参照する

decorator内でも @login_required(login_url='')で指定ができる
次に認証成功した時は'next'にリダイレクトパスが保存されているが、
これを変更したい時は次のように行う

`@login_required(redirect_filed_name='my_redirect_filed')`

# user.is_authentiacted

function viewではlogin_requiredのdecroraterを利用することができたが、class viewでは使えない
そのためjinja2上で次を追加することで対策をとる
これはrequest methodのuserを参照して、User objectでのセッション情報と比較して確認される（はず）

`{% if user.is_authenticated %}`

viewsで`autenticate(request, username, password)`で登録されたやつ。

## login user
loginしているuserはrequestから取れる
例えば次のようなサンプルがあげられる

```.py
user = request.user.get_username()
```