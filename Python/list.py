l = [0, 1, 2, 3, 4, 5]


# .append
l = [0, 1, 2, 3, 4, 5]
l.append(6)
print(l)    # [0, 1, 2, 3, 4, 5, 6]

l.append([7, 8, 9])
print(l)    # [0, 1, 2, 3, 4, 5, 6, [7, 8, 9]]

l = l + [7, 8, 9]   # [0, 1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9]
print(l)

# .insert
l = [0, 1, 2, 3, 4, 5]
l.insert(0, 'a')
print(l)    # ['a', 0, 1, 2, 3, 4, 5]

l = l[:2] + ['b', 'c'] + l[2:]
print(l)    # ['a', 0, 'b', 'c', 1, 2, 3, 4, 5]

# .remove
l.remove(0)
print(l)    # ['a', 'b', 'c', 1, 2, 3, 4, 5]

l.remove('b')
print(l)    # ['a', 'c', 1, 2, 3, 4, 5]

# del
l = ['a', 'b', 'c', 'd', 'e']
del l[2]
print(l)    # ['a', 'b', 'd', 'e']

del l[1:2]
print(l)    # ['a', 'd', 'e']

# .pop
l = [0, 1, 2, 3, 4, 5]
l.pop() # [0, 1, 2, 3, 4]
print(l)

l.pop() # [0, 1, 2, 3]
print(l)

