

## @login_required
    from django.contrib.auth.decorators import login_required

    を利用してviewsでdecoratorで使うと楽チン
    要はis_authenticatedかどうかを評価する
    notの時はredirect先としてsettings.pyのLOGIN_URLを参照する

    decorator内でも @login_required(login_url='')で指定ができる
    次に認証成功した時は'next'にリダイレクトパスが保存されているが、
    これを変更したい時は次のように行う
    @login_required(redirect_filed_name='my_redirect_filed')