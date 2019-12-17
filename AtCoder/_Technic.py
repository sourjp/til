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