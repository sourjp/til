a, b = map(str, input().split())
ab = a + b
print('Yes' if int(ab) == int(int(ab)**(1/2)) ** 2 else 'No')
