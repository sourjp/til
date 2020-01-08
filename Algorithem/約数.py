'''
約数とは与えられた二つの数値に対して共通して割り切れる事をさす。
例えば XとYが与えられた X % a == 0 and Y % a == 0 の関係となる。
一つの性質として二つの値が与えられた時に最大あたいは必ずXとYの小さい値の半分以下である。
Y <= 2/X(Y > X)　例えばYが100ならばXは50が最大ということ。
つまりこの計算の最後の結果が最大公約数となる。
そしてもう一つ言えることが、この最大公約数以下が二つの数値の約数のリストとなる。

注意点として次の方法ではO(n/2)、つまりO(n)の計算量となってしまう。
'''

def divisor(x, y) -> list:
    min_num = min(x, y)
    i = 1
    div_list = []
    while i < min_num+1:
        if x % i == 0 and y % i == 0:
            div_list.append(i)
        i += 1
    return div_list

print(divisor(420, 660)) # [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

'''
最大公約数を求めるにはユークリッドの互除法というアルゴリズムがある。
これは互いに割り算を行いその余りを割っていくことで最後に割り切れた数字が０になるというアルゴリズム。
この場合は互いに割っていくためO(logn)の計算量で求めることができる
'''

def euclid(x, y) -> int:
    a = max(x, y)
    b = min(x, y)

    while a > 0 and b > 0:
        b, a = a % b, b

    return a

print(euclid(420, 660)) # 60

import fractions
print(fractions.gcd(420, 660))

import math
print(math.gcd(420, 660))