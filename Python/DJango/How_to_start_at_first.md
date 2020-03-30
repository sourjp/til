# Djangoのプロジェクト開始
    django-admin startproject .

    次のようにするとconfigという名前でproject folderが作れる
    django directoryの構造をどうするかによる

    django-admin strartproject config .

# Djangoのアプリ開始
    django-admin startapp APPNAME

    アプリケーションを作成するフォルダが作れる

# makemigrationの実施
    python manage.py makemigrations

    DBマイグレーションの設定

# migrationの実施
    python manage.py migrate

    migrationファイルの適用

    次の方法でDBにアクセスできる
    python manage.py shell



