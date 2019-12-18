def func1(a, b):
    ''' O(n) + O(2logn)
    大文字、小文字の区別がつくので、考慮しないならupper or lowerで変換が必要

    '''
    if len(a) != len(b):
        return -1

    #a = a.upper()
    #b = b.upper()

    a = list(a)
    b = list(b)

    a = sorted(a)
    b = sorted(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            return 'No'
    
    return 'Yes'


def func2(a, b):
    ''' O(1) + O(2n)
    ASCII 前提であれば文字コードのhash tableを利用するので大文字、小文字が区別される
    最後が0であれば文字列は同じ
    '''
    if len(a) != len(b):
        return -1

    dp = [0 for i in range(128)]

    for aa in a:
        dp[ord(aa)] += 1
        
    for bb in b:
        dp[ord(bb)] -= 1
        if dp[ord(bb)] < 0:
            return 'No'

    result = sum(dp)
    if result == 0:
        return 'Yes'
    else:
        return 'No'

    

a = 'God '
b = 'god '

print(func1(a, b))
print(func2(a, b))