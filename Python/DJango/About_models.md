# Simpleなmodels

models.Modelを継承して作成する

```.py
from django.db import models

class TestModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()

    def __str__(self):
        return self.title
```

・makemigrations
models.pyで作成したDBの変更から、DBに設定するためのファイルを作成してくれる
記録してくれるので、バックアップにもなるし、validationもかけてくれる

新しいFieldを追加するときに元のdataがあった場合はそこにはnullが入ってしまう
しかしデフォルトではDB filedはnull=Falseになっているのでfieldが追加できない
この場合はエラーが出てどうするか聞かれるので設定する
1.nullではなくデフォルトデータを手動で設定する
2.自分でmodels.pyを設定し直す



・migrate
作成したmakemigrationsの結果をDBに反映させる
また初期のmigrateではデフォルトの設定を反映させるので色々出る。authとか。
つまりadminログインなどはtableを作らないとできないので、まずこれが必要(create super user)

・id
デフォルトでprimary keyとしてidが設定される

・Admin管理
adminで作成したDBを管理したければadmin.pyにregisterすること

また DB tableでstrを設定することでADMIN DB上での表示名を変えることができる

```admin.py
from .models import TestModel

admin.site.register(TestModel)
```

# User Obejct
Djangoには事前に組み込みされているobjectが用意されている  
その一つとしてUser Objectがある

```Views.py
from django.shortcuts import render
from django.contrib.auth.models import User

def signupunfc(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(requests, 'test.html', {'error': ’このユーザーは登録されています'})

        except:
            user = User.objects.create_user(username, email, password)
            return render(xxx)
            
    return render(xxx)
```

DjangoではUserテーブルが重複している場合はerrorがerrorで重複していると出る
ただエラー画面がユーザーに見えてしまうので、try/execeptを利用する
そしてerror contextを与えてあげれば、jinja側で{% if error %}の処理を加えることができる


# Objectへのクエリー
・全てのデータをとりたいとき
e.g. User.objects.all()

・指定したいとき
e.g. User.objects.get(username=xxx)


