def divide(n):
    if len(str(n)) <= 1:
        return n

    out = n % 10
    
    return out + divide(n//10)

n = int(input())
sn = divide(n)

print('Yes' if int(n) % sn == 0 else 'No')

'''
n = input()
sn = sum(map(int, n))

print('Yes' if int(n) % sn == 0 else 'No')
'''
