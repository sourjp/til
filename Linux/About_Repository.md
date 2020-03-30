# Repository
ソフトウェアには初めから追加ソフトウェアのインストール先の情報が組み込まれている
要はソフトウェアをダウンロードする先のリストであるデータベースみたいなもの

しかし最初から入っているので、最新の情報にはなっていない
そのためレポジトリを更新する必要がある

EPELレポジトリ
    RHEL向けの追加パッケージ関連

Remiレポジトリ
    MysqlやPHPなどのソフトウェア関連


Ubuntuならapt, CentOSやRHELならyum
```.sh
yum update
yum upgrade
```

```.sh
*CentOS
yum install REPOSITORY_URL
cat /etc/yum.repost.d/*

*Ubuntu
cat /etc/apt/sources.list
```

上のディレクトリにレポジトリ情報が登録されているのでenabled=1を使うやつなので、必要に応じて0にする



