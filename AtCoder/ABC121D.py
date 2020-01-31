# aが偶数の時a^(a+1)は1になる性質。例えば100 ^ 101 = 001
# なぜなら偶数の最後は必ず0になる。つまり桁上がりせずに末尾に1が付与される
# このことからXORを行うと必ず末尾のみ1になる性質である。

a, b = map(int, input().split())
if a%2 == b%2: # 3, 4, 5  => 3^1 / 4, 5, 6 => 1^6
    k = (b-a)//2
    print(b^(k%2) if a%2==0 else a^(k%2))
elif a%2 == 0 and b%2 == 1: # 4, 5, 6, 7 => 1^1
    print(((b-a+1)//2)%2)
elif a%2 == 1 and b%2 ==0: # 3, 4, 5, 6 => 3^1^6
    print(a^b^((b-a-1)//2)%2)

'''
bit = ['0' for _ in range(41)]
while a <= b:
    val = bin(a)[2:]
    for i in range(1, len(val)+1):
        if val[-i] == '1' and bit[-i] == '0': bit[-i] = '1'
        elif val[-i] == '1' and bit[-i] == '1': bit[-i] = '0'
    a += 1
print(int(''.join(bit), 2))
'''