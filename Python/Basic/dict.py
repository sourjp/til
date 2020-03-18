t1 = {}
t1['jack'] = 4098

t2 =  {'jack': 4098, 'sape': 4139}

print(t1)   # {'jack': 4098}
print(t2, t2['jack'])   # {'jack': 4098, 'sape': 4139} 4098
print(list(t2)) # ['jack', 'sape']

print('jack' in t2)
del t2['jack']
print(t2)
print('jack' in t2)

t3 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])    # {'sape': 4139, 'guido': 4127, 'jack': 4098}
t4 = dict(sape=4139, guido=4127, jack=4098) # {'sape': 4139, 'guido': 4127, 'jack': 4098}
t5 = {x: x**2 for x in (2, 4, 6)}   # {2: 4, 4: 16, 6: 36}

print(t3)
print(t4)
print(t5)

for k, v in t4.items():
    print(k, v)

# sorted
print(sorted(t4))

# get
print(t4.get('jack'))
print(t4.get('lucy'))
print(t4.get('lucy', 'i can\'t find her'))