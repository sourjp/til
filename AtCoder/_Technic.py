'''
最大公約数を求める方法
    python v3.5~からはimport math
'''
import fractions
def gcdcheck(a, b):
    return fractions.gcd(a, b)

'''
最小公倍数を求める方法
   python v3.5~からはimport math
'''
import fractions
def lcm(a,b):
    return a * b // fractions.gcd(a,b)

'''
eval関数    
    計算式をstringで渡すと、計算してくれる
'''
A, B, C, D = map(str, input())

op = ['+', '-']
for op1 in op:
    for op2 in op:
        for op3 in op:
            result = A+op1+B+op2+C+op3+D
            if eval(result) == 7:
                print(result + '=7')
                exit()

'''
二次元配列になるように受け取る方法
'''
Row=int(input())

List=[list(map(int,input().split())) for i in range(Row)]
# 1 わかりやすい

List=[[int(j) for j in input().split()] for i in range(Row)]
# 2 分かりづらい

List=[]
for i in range(Row):
    List.append(list(map(int,input().split())))
# 3 基本形


'''
桁あたりを数値として取得して計算する方法
'''
n, a, b = map(int, input().split())

ans = 0
cnt = 0
for i in range(a, n+1):
    res = 0
    num = i
    while num > 0:
        res += num % 10
        num //= 10

    if res >= a and res <= b:
        ans += i

print(ans)


'''
chrセットにASCIIコードの数字を当てると数字を文字に変更できる
'''
String="abc"
[print(chr(i), end=" ") for i in range(ord('a'), ord('z')+1) if chr(i) not in String]

[print(chr(i), end=" ") for i in range(ord('a'), ord('z')+1)]


'''
A-Z, a-zを取得する方法
'''

### patern1
import string
letters = string.ascii_lowercase
print(letters)  # abcdefghijklmnopqrstuvwxyz



### patern2
print(sorted(map(chr,range(97,123)))) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

### patern3
print(sorted(map(chr,range(65,91)))) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

