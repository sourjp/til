l = [0, 1, 2, 3, 4, 5]

# basic
print('*' * 20)
print(l[0]) # 0
print(l[-1])    # 5
print(l[:4])    # [0, 1, 2, 3]
print(l[2:])    # [2, 3, 4, 5]
print(l[2:4])   # [2, 3]
print(l[:]) # [0, 1, 2, 3, 4, 5]


# connect
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
print(l + [6, 7, 8])    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(l[:2] + [6, 7, 8] + l[2:])    # [0, 1, 6, 7, 8, 2, 3, 4, 5]


# replace
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l[1:-1] = [11, 22, 33, 44]
print(l)    # [0, 11, 22, 33, 44, 5]


# .append
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l.append(6)
print(l)    # [0, 1, 2, 3, 4, 5, 6]

l.append([7, 8, 9])
print(l)    # [0, 1, 2, 3, 4, 5, 6, [7, 8, 9]]


# .insert
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l.insert(0, 'a')
print(l)    # ['a', 0, 1, 2, 3, 4, 5]

l = l[:2] + ['b', 'c'] + l[2:]
print(l)    # ['a', 0, 'b', 'c', 1, 2, 3, 4, 5]


# .remove
print('*' * 20)
l.remove(0)
print(l)    # ['a', 'b', 'c', 1, 2, 3, 4, 5]

l.remove('b')
print(l)    # ['a', 'c', 1, 2, 3, 4, 5]


# del
print('*' * 20)
l = ['a', 'b', 'c', 'd', 'e']
del l[2]
print(l)    # ['a', 'b', 'd', 'e']

del l[1:2]
print(l)    # ['a', 'd', 'e']


# .pop
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l.pop() # [0, 1, 2, 3, 4]
print(l)

l.pop() # [0, 1, 2, 3]
print(l)

