
# 監視っぽいコマンドいくつか

## 時刻関連
```uptime.sh
sourjp@kind:~$ uptime
 05:52:06 up 2 days, 18:30,  1 user,  load average: 0.00, 0.00, 0.00
```

## Diskやファイルサイズ関連
```df.sh
sourjp@kind:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            830M     0  830M   0% /dev
tmpfs           169M  908K  168M   1% /run
/dev/sda1        39G   10G   29G  26% /
tmpfs           844M     0  844M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           844M     0  844M   0% /sys/fs/cgroup
/dev/loop0       67M   67M     0 100% /snap/google-cloud-sdk/105
/dev/loop2       90M   90M     0 100% /snap/core/7917
/dev/sda15      105M  3.6M  101M   4% /boot/efi
/dev/loop4       92M   92M     0 100% /snap/core/8689
/dev/loop3       93M   93M     0 100% /snap/google-cloud-sdk/123
tmpfs           169M     0  169M   0% /run/user/1002
```


```du.sh
sourjp@kind:~$ du -ah /var/ | more

12K	/var/tmp
4.0K	/var/backups/dpkg.diversions.4.gz
4.0K	/var/backups/apt.extended_states.2.gz
4.0K	/var/backups/dpkg.diversions.1.gz
4.0K	/var/backups/dpkg.statoverride.0
4.0K	/var/backups/dpkg.statoverride.1.gz
32K	/var/backups/apt.extended_states.0
52K	/var/backups/alternatives.tar.0
```

## メモリ関連
```free.sh
sourjp@kind:~$ free
              total        used        free      shared  buff/cache   available
Mem:        1727568      255012      246320         920     1226236     1286840
Swap:             0           0           0

sourjp@kind:~$ free -m
              total        used        free      shared  buff/cache   available
Mem:           1687         248         240           0        1197        1256
Swap:             0           0           0
```

## プロセス関連
```top.sh
sourjp@kind:~$ top

top - 05:56:39 up 2 days, 18:35,  1 user,  load average: 0.00, 0.00, 0.00
Tasks: 100 total,   1 running,  62 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.1 us,  0.1 sy,  0.1 ni, 99.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1727568 total,   246092 free,   254784 used,  1226692 buff/cache
KiB Swap:        0 total,        0 free,        0 used.  1287068 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND                                                                      
    1 root      20   0  160052   9488   6868 S  0.0  0.5   0:09.66 systemd  
```

## システム負荷
各種のついて確認できる

```vmstat.sh
sourjp@kind:~$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 246324  28348 1198404    0    0     6    15   12   41  0  0 100  0  0
 0  0      0 246316  28348 1198404    0    0     0     0   26   77  0  0 100  0  0
^C

sourjp@kind:~$ vmstat -SM
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0    240     27   1170    0    0     6    15   12   41  0  0 100  0  0
```

## プロセス
```ps.sh
sourjp@kind:~$ ps aux | head 
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.5 160052  9488 ?        Ss   Mar20   0:09 /lib/systemd/systemd --system --deserialize 35
root         2  0.0  0.0      0     0 ?        S    Mar20   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        I<   Mar20   0:00 [rcu_gp]
root         4  0.0  0.0      0     0 ?        I<   Mar20   0:00 [rcu_par_gp]
root         6  0.0  0.0      0     0 ?        I<   Mar20   0:00 [kworker/0:0H-kb]
root         8  0.0  0.0      0     0 ?        I<   Mar20   0:00 [mm_percpu_wq]
root         9  0.0  0.0      0     0 ?        S    Mar20   0:01 [ksoftirqd/0]
root        10  0.0  0.0      0     0 ?        I    Mar20   0:02 [rcu_sched]
root        11  0.0  0.0      0     0 ?        S    Mar20   0:00 [migration/0]
```