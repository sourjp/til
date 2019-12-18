def func1(ll):
    ''' O(N), O(N) mem
    '''
    hs = []
    for i in range(len(ll)):
        if ll[i] in hs:
            continue
        else:
            hs.append(ll[i])

    return hs


def func2(ll):
    ''' O(n^2), O(1) mem
    '''
    i = 0
    while i < len(ll):
        j = i + 1
        while j < len(ll):
            if ll[i] == ll[j]:
                del ll[j]
            j += 1
        i += 1
    return ll

test = ['a', 'i', 'u', 'e', 'a', 'u', 'e', 'o', 'a']

print(func1(test))
print(func2(test))