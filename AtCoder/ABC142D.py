import fractions

a, b = map(int, input().split())

import math
def prime_number(n):
    prime_list = []
    p = 2
    last = n

    while p <= math.sqrt(last)+1:
        cnt = 0
        if n % p != 0: pass
        else:
            while n % p == 0:
                n //= p
                cnt += 1

            prime_list.append((p, cnt))

        p += 1
    
    if n != 1: prime_list.append((p, cnt))
    return len(prime_list)

n = fractions.gcd(a, b)
print(prime_number(n) + 1)