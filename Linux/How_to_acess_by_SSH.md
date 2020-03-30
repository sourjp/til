# SSH

## 鍵の作成  
`ssh-keygen -t rsa -v`

~/.sshに鍵が生成される  
.pubが公開鍵なので、これをサーバーに配置する

## サーバーの鍵の置く場所

同様に ~/.ssh に配置する(chown700)

## 鍵を送信する  
SCPで送ってあげる  
`scp ~/.ssh/id_rsa.pub test@192.168.0.1:~/.ssh/authorized_keys`

## 鍵を使ってログインする  
`ssh -i ~/.ssh/id_rsa test@192.168.0.1`

## SSH側の設定

次のような方法でSSHのセキュリティをあげる  
・ポート番号の変更  
・空白パスワード禁止  
・パスワードログイン禁止  
・ルートログイン禁止

```/etc/ssh/sshd_config.sh
Port 2022

# PasswordAuthentication yes

PermitEmptyPasswords no

PasswordAuthentication no

PermitRootLogin no
```

終わったら`sudo systemctl restart sshd`で反映させる  
ただしここではportが空いてないのでfirewallを開ける!!

