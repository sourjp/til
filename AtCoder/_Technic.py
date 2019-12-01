
'''
最小公倍数を求める方法
   python v3.5~からはimport math
'''
import fractions
def lcm(a,b):
    return a * b // fractions.gcd(a,b)
