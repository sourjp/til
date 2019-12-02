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


# .append , .extend
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l.append(6)
print(l)    # [0, 1, 2, 3, 4, 5, 6]

l.append([7, 8, 9])
print(l)    # [0, 1, 2, 3, 4, 5, 6, [7, 8, 9]]

l.extend([1, 1, 1, 1])
print(l)

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

del l[:]    # []
print(l)

del l
#print(l)    # NameError: name 'l' is not defined

# clear
print('*' * 20)
l = ['a', 'b', 'c', 'd', 'e']
l.clear()
print(l)    # []

# .pop
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
l.pop() # [0, 1, 2, 3, 4]
print(l)

l.pop() # [0, 1, 2, 3]
print(l)

# .count
print('*' * 20)
l = [0, 1, 2, 3, 1, 2]
count = l.count(1)
print(count)    # 2

# .reverse
print('*' * 20)
l = [0, 1, 2, 3, 4, 5]
print(l[::-1])
l.reverse() # [0, 1, 2, 3, 4]
print(l)

# .copy // shallowcopy
print('*' * 20)
l = [0, 1, 2, 3, [4, 5]]
ll = l.copy()
print(ll)
l.pop()
print(l)
print(ll)

# list.sort(key=None, reverse=False)
# https://docs.python.org/ja/3/howto/sorting.html#sortinghowto

# list Stack
#   list.append(), list.pop()で管理すればOK

# list Queue
#   https://docs.python.org/ja/3/tutorial/datastructures.html
from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)                    # deque(['Eric', 'John', 'Michael'])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves 'Eric'
queue.popleft()                 # The second to arrive now leaves 'John'
print(queue)                    # Remaining queue in order of arrival // deque(['Michael', 'Terry', 'Graham'])


# list内包表記

squares = [x**2 for x in range(10)]
print(squares)

num_list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(num_list)