# def, no return
def fib1(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

print(fib1(100))

# def, with return
def fib2(n):
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l

f22 = fib2
f2 = fib2(100)
print(fib2)
print('fib2:', fib2(100))
print('f2:', f2)
print('f22:', f22(100))

'''
# def, default args
def ask_ok(responce, retries=4, reminder='Please try again!'):
    while True:
        ok = responce
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user responce')
        print(reminder)
        responce = input('retry:')
ans = input('try:')
print(ask_ok(ans))
'''

# other1
i = 5
def f(arg=i):
    print(arg)
i = 6
f() # 5 not 6

# other2
def f1(a, l=[]):
    l.append(a)
    return l

print(f1(1)) # [1]
print(f1(2)) # [1, 2]
print(f1(3)) # [1, 2, 3]

def f2(a, l=None):
    if l == None:
        l = []
    l.append(a)
    return l

print(f2(1)) # [1]
print(f2(2)) # [2]
print(f2(3)) # [3]

# def, *name(tuple) **name{dict}
def save(name='test', *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

save('t1', 
     't2', 4, 't3',
     aaa='1', bbb='2')