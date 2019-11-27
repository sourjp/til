# Basic
print('*' * 20)
words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word))

print('*' * 20)
users = {'Jane': 'inactive', 'Ken': 'active', 'Tom': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'inactive':
        pass
    elif status == 'active':
        active_users[user] = status
print('users', users)   # users {'Jane': 'inactive', 'Ken': 'active', 'Tom': 'active'}
print('active_users', active_users) # active_users {'Ken': 'active', 'Tom': 'active'}

# break, continue
for i in range(10):
    if i % 2 == 0:
        continue
    elif i == 9:
        break
    else:
        print(i, end=" ")   # 1 3 5 7 
print('')

# for, range
print('*' * 20)
a = range(10)
print(type(a))  # <class 'range'>
print(a)    # range(0, 10)

for i in range(10):
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9 
print('')

for i in range(5, 10):
    print(i, end=' ')   # 5 6 7 8 9 
print('')

for i in range(1,10,3):
    print(i, end=' ')   # 1 4 7 
print('')

for i in range(-10, -100, -20):
    print(i, end=' ')   # -10 -30 -50 -70 -90 
print('')

# range adv
print('*' * 20)
box = range(5)
print(box)  # range(0, 5)
print(sum(box)) # 10
print(list(box))    # [0, 1, 2, 3, 4]

# for enumerate
print('*' * 20)
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(5):
    print(i, a[i] , end=', ') # 0 Mary, 1 had, 2 a, 3 little, 4 lamb, 
print('')

for index, value in enumerate(a):
    print(index, value, end=', ') # 0 Mary, 1 had, 2 a, 3 little, 4 lamb, 
print('')



