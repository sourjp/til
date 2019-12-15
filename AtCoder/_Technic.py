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