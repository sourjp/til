# user追加
useraddでuserを追加して、userの確認は/etc/passwdをみる

削除するときはuserdel。

```.sh
sourjp@kind:~$ sudo useradd test123

sourjp@kind:~$ cat /etc/passwd | grep test123
test123:x:1004:1006::/home/test123:/bin/sh

sourjp@kind:~$ sudo passwd test123
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully

sourjp@kind:~$ sudo userdel test123

sourjp@kind:~$ cat /etc/passwd | grep test123

```

# 管理者ユーザー作成
root配下に管理者ユーザーを追加する

```visudo.sh
# User privilege specification
root    ALL=(ALL:ALL) ALL
administrator    ALL=(ALL:ALL) ALL
```
