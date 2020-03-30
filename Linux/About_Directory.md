# Directories
基本はこれ。ユーザー単位でディレクトリの配下に同じようの構造が広がる。

/       Root directory  
/bin    バイナリファイルや実行プログラム  
/etc    システムの設定ファイルをおいたディレクトリ  
/home   各ユーザー向けのホームディレクトリ  
/opt    Linux以外のソフトウェアをインストール  
/tmp    bootの時に削除されるディレクトリ  
/usr    userに関連するプログラム /usr/binなど  
/var    logなど様々なデータ
  
ベースのOSに含まれないアプリケーションは　/opt　か、　/usr/local に保存される


# Command
・dir作成
mkdir tmpdir
mkdir -p tmpdir/1/2/3

・dir削除
rmdir tmpdir
rmdir -p tmpdir/1/2/3

・再帰的にdir削除
rm -rf tmpdir

・ディレクトリだけ表示   
ls -d

・最新のファイルから一覧ソートができる  
ls -latr


# Attributes
次の形でディレクトリに属性が設定されている

Permissions, Number of links, Owner Name, Group Name, Number of bytes inthe file, Last modification time, File Name
```.sh
sourjp@kind:~$ ls -l
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp
```

ls -F でファイルタイプが確認できる

/ Directory  
@ Link  
`*` Executable

# Permissions
-rw-rw-r-- など10個の表示で表される  
Type(1), User(3), Group(3), Other(3)が組み合わさったもの

一つ目はファイルの種類  
・- RefularFile  
・d Directory  
・l SymbolicLink

最後は３つ単位でぎの内容が含まれる
・r   Read  
・w   Write  
・x   Execute  

その３つは次のカテゴリーに別れる  
・u User
・g Group  
・o Other  
・a All  

上のカテゴリーには次のようにuser, groupsが管理されている
```.sh
sourjp@kind:~$ id
uid=1002(sourjp) gid=1003(sourjp) groups=1003(sourjp),4(adm),20(dialout),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(lxd),114(netdev),1000(ubuntu),1001(google-sudoers)

sourjp@kind:~$ groups
sourjp adm dialout cdrom floppy audio dip video plugdev lxd netdev ubuntu google-sudoers
```

## chmod
これらを変更するにはこのコマンドを利用して次を引数として与える  
・ugoa 対象とするカテゴリーを選ぶ   
・+-= Add, Subtract, Setを選ぶ  
・rwx 権限を選ぶ

```.sh
sourjp@kind:~$ ls -l
total 4
-rw-rw-r-- 1 sourjp sourjp    0 Mar 21 07:57 test.txt
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp

sourjp@kind:~$ chmod o+x test.txt 

sourjp@kind:~$ ls -l
total 4
-rw-rw-r-x 1 sourjp sourjp    0 Mar 21 07:57 test.txt
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp

sourjp@kind:~$ chmod u+rwx,o-x test.txt 

sourjp@kind:~$ ls -l
total 4
-rwxrw-r-- 1 sourjp sourjp    0 Mar 21 07:57 test.txt
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp

sourjp@kind:~$ chmod a=r test.txt 

sourjp@kind:~$ ls -l
total 4
-r--r--r-- 1 sourjp sourjp    0 Mar 21 07:57 test.txt
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp

sourjp@kind:~$ chmod a=r,o= test.txt 

sourjp@kind:~$ ls -l
total 4
-r--r----- 1 sourjp sourjp    0 Mar 21 07:57 test.txt
drwxrwxr-x 2 sourjp sourjp 4096 Mar 21 07:36 tmp
```

これらはbinary(2進数)、もしくはDecimal(10進数)、OctalもOK

Octalでは 755 = -rwxr-xr-x みたいにできる


## umask
これはファイルやディレクトリを作成する際のデフォルト権限を指定する

```.sh
sourjp@kind:~$ umask
0002

sourjp@kind:~$ umask -S
u=rwx,g=rwx,o=rx
```

この数字はdefaultの権限から引き算するという考え方  
Directoryは777でFileは666なので  
umask 022ならdirecotryは755でfileは644になる  


## chgrp
ファイルのgroupを変えたい時はこれ

## find

`find DIRECTORY -name FILENAME`

locateの方法あり、これはcronでlinuxが検索用DBを作成しており、それを参照するから
つまり、locateは高速に調べられるがリアルタイムの検索にはならない。


