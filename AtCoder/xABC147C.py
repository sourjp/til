n = int(input())
sentences = [[] for i in range(n)]

for i in range(n):
    nn = int(input())

    for j in range(nn):
        p, t = map(int, input().split())
        sentences[i].append([p - 1, t])

ans = 0
count = 0
for i in range(2 ** n):
    check = {}
    success = True
    for j in range(n):
        # print('i, j:', i, j, bin(i))
        if ((i >> j) & 1):
            sentence = sentences[j]

            for pp, tt in sentence:
                if pp in check:
                    if check[pp] == tt:
                        pass                         
                    else:
                        success = False
                        break
                else:
                    check[pp] = tt
            #print(check)
        else:
            sentence = sentences[j]

            for pp, tt in sentence:
                if pp in check:
                    if check[pp] != tt:
                        pass                         
                    else:
                        success = False
                        break
                else:
                    if tt == 1:
                        check[pp] = 0
                    else:
                        check[pp] = 1

        if success == False:
            # print('break')
            break

    if success:
        # print(check)
        count = bin(i).count('1')    
        ans = max(ans, count)

    # print('c, a:', count, ans)

print(ans)

'''
n = int(input())
messages = [[] for i in range(n)]

for i in range(n):
    num = int(input())

    for j in range(num):
        person, truth = map(int, input().split())
        messages[i].append([person-1, truth])

print(messages)
ans = 0
for i in range(2**n):
    check = i
    count = sum([(check >> t) & 1 for t in range(n)])
    if count <= ans:
        continue
    possible = True
    for k in range(n):
        if (check >> k) & 1:  # k is truth
            message = messages[k]

            for person, truth in message:
                if (check>>person)&1 == truth:
                    continue
                else:
                    possible = False
                    break
        else:  # k is not truth
            continue

        if not possible:
            break

    if possible:
        ans = max(ans, count)

print(ans)
'''