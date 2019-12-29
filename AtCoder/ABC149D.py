n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

cnt = 0
memory = [None] * k

# r なら p　をだす、 s なら r　をだす, p なら s　をだす
for i in range(len(t)):
    if t[i] == 'r':
        if memory[i%k] != 'p':
            memory[i%k] = 'p'
            cnt += p
        elif i == len(t)-1: break
        else:
            if i+k < len(t):
                if t[i+k] == 's':
                    memory[i%k] = 's'
                else:
                    memory[i%k] = 'r'

    elif t[i] == 's':
        if memory[i%k] != 'r':
            memory[i%k] = 'r'
            cnt += r
        elif i == len(t)-1: break
        else:
            if i+k < len(t):
                if t[i+k] == 'p':
                    memory[i%k] = 'p'
                else:
                    memory[i%k] = 's'



    elif t[i] == 'p':
        if memory[i%k] != 's':
            memory[i%k] = 's'
            cnt += s
        elif i == len(t)-1: break
        else:
            if i+k < len(t):
                if t[i+k] == 'r':
                    memory[i%k] = 'r'
                else:
                    memory[i%k] = 'p'

print(cnt)