S = list(input())
T = list(input())

ANS = False
save_left = 0
save_right = 0
for i in range(len(S) - len(T) + 1):
    count = 0
    left = i
    right = i + len(T)

    for sv, tv in zip(S[left:right], T):
        if sv != tv and sv != '?':
            break
        count += 1

    if count == len(T):
        save_left = left
        save_right = right
        ANS = True
     
if ANS:
    S[save_left:save_right] = T
    for w in S:
        if w == '?':
            print('a', end='')
        else: 
            print(w, end='')
else:
    print('UNRESTORABLE')