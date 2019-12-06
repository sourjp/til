s = input()
k = int(input())

turn_on = True
for i in range(min(len(s), k)):
    if s[i] == '1':
        continue
    else:
        print(s[i])
        turn_on = False
        break

if turn_on:
    print('1')