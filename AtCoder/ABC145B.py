n = int(input())
s = input()

half_index = n // 2
right_index = n - half_index

if n == 1 or n % 2 == 1:
    print('No')
elif s[:half_index] == s[right_index:]:
    print('Yes')
else:
    print('No')
