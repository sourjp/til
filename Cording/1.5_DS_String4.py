def base_func(word1, word2):
    if len(word1) == len(word2):
        return check_same(word1, word2)
    elif len(word1) == len(word2)+1:
        return add_insert(word1, word2)
    elif len(word1)+1 == len(word2):
        return add_insert(word2, word1)

    return 'No'

def check_same(word1, word2):
    checker = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if checker == True:
                return 'No'

            checker = True

    if checker: return 'Try Replase Operation'
    else: return 'No Operations is needed'

def add_insert(longw, shortw):
    i = 0
    j = 0
    checker = False

    while i < len(longw):
        if j == len(shortw):
            if checker == False:
                return 'Try Insert Operation'

        if longw[i] != shortw[j]:
            if checker:
                return 'No'
            i += 1

            if longw[i] != shortw[j]:
                return 'No'
        i += 1
        j += 1

    return 'Try Add or Del Operation'

print(base_func('pales', 'paes'))
print(base_func('pales', 'pas'))
print(base_func('pales', 'pares'))
print(base_func('pales', 'pales'))
print(base_func('pales', 'paless'))
