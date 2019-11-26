'''
- INPUT:
6
5 6 4 2 1 3

- OUTPUT:
['1', '6', '4', '2', '5', '3']
['1', '2', '4', '6', '5', '3']
['1', '2', '3', '6', '5', '4']
['1', '2', '3', '4', '5', '6']
['1', '2', '3', '4', '5', '6']
['1', '2', '3', '4', '5', '6']
has exchanged: 4

'''

n = int(input())
l = list(input().split())

i = 0
j = 0
k = 0
c = 0

while i < n:
    min = l[i]
    k = i
    while j < n:
        if min > l[j]:
            min = l[j]
            k = j
        j += 1
    if l[i] == l[k]:
        None
    else:
        l[i], l[k] = l[k], l[i]
        c += 1
    i += 1
    j = i
    print(l)
print('has exchanged:', c)