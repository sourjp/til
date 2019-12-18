def func1(words):

    ans = []
    cnt = 1
    for i in range(1, len(words)):
        if i == len(words)-1:
            cnt += 1
            ans.append(words[i-1])
            ans.append(str(cnt))
        
        elif words[i-1] != words[i]:
            ans.append(words[i-1])
            ans.append(str(cnt))
            cnt = 0

        cnt += 1

    ans = ''.join(ans)
    return ans if len(ans) < len(words) else words
    
words = 'aabcccccaaa'
words2 = 'abcdefg'
print(func1(words))
print(func1(words2))