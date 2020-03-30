# PATH

Linuxのコマンドを利用する際にどのディレクトリを参照するか？を示す
厳密には実行するbinaryファイルを探すディレクトリを指定している

またwhichを利用することでどのdirectoryのバイナリファイルを参照しているかがわかる  
例えば/usr/local/binにも同じ名前のバイナリファイルがあった場合に参照するのはPATHの先頭から見ていくので注意  
他にもPATHに存在しないディレクトリにバイナリファイルをおいてももちろん実行してくれない

```.sh
root@kind:/# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

root@kind:/# env | grep PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

root@kind:/# which cat
/bin/cat

root@kind:/# ls /bin/cat
/bin/cat
``