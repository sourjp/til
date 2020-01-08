'''
素数の定義： 1とその数字のみで割り切れるもの (1, 2, 3, 5, 7...)
またその最大値は√nになる。n = 100ならば10 * 11 < nとなり対象の値を超えてしまうため。
このことから与えられた数値から素数を求めることはO(logn)で求められる
'''
import math

def prime_number(n) -> bool:
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    
    return True

print(prime_number(10)) # False
print(prime_number(13)) # True


'''
素因数分解：　与えられた数字を素数で分解すること。例えば 60 = 2^2 + 3^1 + 5^1 といったこと。
なぜ素数かというと、例えば2, 4であれば2, 2^2で分解できる。つまり2で累乗を計算する際に、その倍数は計算として含まれるため。
このことから素因数分解はO(logn)で求められる。基数は素数によって厳密に異なるが、その数値で割られていくためO(logn)と考えられる

仮に60で計算すると[(2, 2), (3, 1), (5, 1)]という結果になる。
このことから60は2, 3, 5を組み合わせた約数を持っていると言えるが、
素数という1と自分の値だけという性質を考えると素数は 2, 3, 5という結果に 1 を追加した、[1, 2, 3, 5]が素数の数となる。

またこの時に注意しなければいけないのは、素数である。素数はそれ自体が素数であるため素因数分解はできない。
よって、次の関数では最後に n != 1　つまり、分解できなかった場合は素数であるため、それをアペンドして返す。
'''

import math
def prime_factorization(n) -> list:
    p = 2
    pf_list = []
    last = n

    while p <= math.sqrt(last):
        cnt = 0

        if n % p != 0: pass
        else:
            while n % p == 0:
                n //= p
                cnt += 1

            pf_list.append((p, cnt))
        p += 1

    if n != 1: pf_list.append((n, 1))

    return pf_list

print(prime_factorization(6)) # [(2, 1), (3, 1)]
print(prime_factorization(60)) # [(2, 2), (3, 1), (5, 1)]
print(prime_factorization(51)) # [(3, 1), (17, 1)]
print(prime_factorization(13)) # [(13, 1)]
