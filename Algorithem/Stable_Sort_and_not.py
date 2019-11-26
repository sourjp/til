# Stable sort by Insert sort
'''
- INPUT:
5
H4 C9 S4 D2 C3

- OUTPUT:
['D2', 'H4', 'C9', 'S4', 'C3']
['D2', 'C3', 'H4', 'C9', 'S4']
['D2', 'C3', 'H4', 'S4', 'C9']
['D2', 'C3', 'H4', 'S4', 'C9']
bubble_sort steps: 7
'''
n = int(input())
l = list(input().split())

i = 1
j = 0

while i < n:
    while j < i:
        if l[i][1] < l[j][1]:
            v = l[i]
            del l[i]
            l.insert(j, v)
            break
        j += 1
    j = 0
    i += 1
    print(l)


# Stable sort by Bubble sort
'''
- INPUT:
5
H4 C9 S4 D2 C3

- OUTPUT:
['D2', 'H4', 'C9', 'S4', 'C3']
['D2', 'C3', 'H4', 'C9', 'S4']
['D2', 'C3', 'H4', 'S4', 'C9']
['D2', 'C3', 'H4', 'S4', 'C9']
bubble_sort steps: 7
'''

n = int(input())
l = list(input().split())

i = 0
j = n - 1
step = 0

while i < n - 1:
    while j > i:
        if l[j][1] < l[j-1][1]:
            step += 1
            l[j], l[j-1] = l[j-1], l[j]
        j -= 1
    j = n - 1
    i += 1
    print(l)
print('bubble_sort steps:', step)            


# Unstable sort by Selection sort
'''
- INPUT:
5
H4 C9 S4 D2 C3

- OUTPUT:
['D2', 'C9', 'S4', 'H4', 'C3']
['D2', 'C3', 'S4', 'H4', 'C9']
['D2', 'C3', 'S4', 'H4', 'C9']
['D2', 'C3', 'S4', 'H4', 'C9']
['D2', 'C3', 'S4', 'H4', 'C9']
has exchanged: 2

'''

n = int(input())
l = list(input().split())

i = 0
j = 0
k = 0
c = 0

while i < n:
    min = l[i][1]
    k = i
    while j < n:
        if min > l[j][1]:
            min = l[j][1]
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