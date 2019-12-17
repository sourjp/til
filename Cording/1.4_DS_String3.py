words = 'Tact Cooa'

def func1(words):
    dp = [0] * 128

    words = words.replace(' ', '').lower()

    for word in words:
        if ord(word) > 128: return 'This is not ASCII code'
        dp[ord(word)] += 1
    
    checker = False
    for d in dp:
        if d % 2 == 1:
            if checker == True: return 'No'
            checker = True

    return 'Yes'

def func2(words):
    dp = [0] * 128

    words = words.replace(' ', '').lower()

    for word in words:
        if ord(word) > 128: return 'This is not ASCII code'

        if dp[ord(word)] == 1: dp[ord(word)] -= 1
        else: dp[ord(word)] += 1
    
    if sum(dp) > 1:
        return 'No'

    return 'Yes'

print(func1(words))
print(func2(words))