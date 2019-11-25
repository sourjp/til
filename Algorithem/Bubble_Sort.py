'''
-INPUT:
5
5 3 2 4 1

- OUTPUT:
['1', '5', '3', '2', '4']
['1', '2', '5', '3', '4']
['1', '2', '3', '5', '4']
['1', '2', '3', '4', '5']
bubble_sort steps: 8
'''

n = int(input())
l = list(input().split())


i = 0
j = n - 1
step = 0

while i < n - 1:
    while j > i:
        if l[j] < l[j-1]:
            step += 1
            v = l[j]
            del l[j]
            l.insert(j-1, v)
        j -= 1
    j = n - 1
    i += 1
    print(l)
print('bubble_sort steps:', step)            