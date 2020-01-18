h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

L = [[0 for _ in range(w)] for _ in range(h)]
R = [[0 for _ in range(w)] for _ in range(h)]
U = [[0 for _ in range(w)] for _ in range(h)]
D = [[0 for _ in range(w)] for _ in range(h)]

def make(L, R, U, D):
    i = 0
    while i < h:
        j = 0
        while j < w:

#    for i in range(h):
#        for j in range(w):
            if s[i][j] == '#':
                L[i][j] == 0
            elif s[i][j] == '.':
                if j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i][j-1] + 1

            ri = i
            rj = w-j-1
            if s[ri][rj] == '#':
                R[ri][rj] == 0
            elif s[ri][rj] == '.':
                if rj == w-1:
                    R[ri][rj] = 1
                else:
                    R[ri][rj] = R[ri][rj+1] + 1
        

            if s[i][j] == '#':
                D[i][j] == 0
            elif s[i][j] == '.':
                if i == 0:
                    D[i][j] = 1
                else:
                    D[i][j] = D[i-1][j] + 1

            ui = h-i-1
            uj = j
            if s[ui][uj] == '#':
                U[ui][uj] == 0
            elif s[ui][uj] == '.':
                if ui == h-1:
                    U[ui][uj] = 1
                else:
                    U[ui][uj] = U[ui+1][uj] + 1
            
            j += 1
        i += 1

'''
    for j in range(w):
        for i in range(h):
            if s[i][j] == '#':
                D[i][j] == 0
            elif s[i][j] == '.':
                if i == 0:
                    D[i][j] = 1
                else:
                    D[i][j] = D[i-1][j] + 1

            ui = h-i-1
            uj = j
            if s[ui][uj] == '#':
                U[ui][uj] == 0
            elif s[ui][uj] == '.':
                if ui == h-1:
                    U[ui][uj] = 1
                else:
                    U[ui][uj] = U[ui+1][uj] + 1
'''


def right(i, j):
    ui = i-1
    di = i+1
    lj = j-1
    rj = j+1
    cnt = 1

    while ui >= 0 and s[ui][j] != '#':
        ui -= 1 
        cnt += 1

    while di < h and s[di][j] != '#':
        di += 1 
        cnt += 1

    while lj >= 0 and s[i][lj] != '#':
        lj -= 1 
        cnt += 1

    while rj < w and s[i][rj] != '#':
        rj += 1 
        cnt += 1
    #print(i, j, ui, di, lj, rj, cnt)
    return cnt

make(L, R, U, D)

ans = 0
print(L)
print(R)
print(U)
print(D)

i = 0
while i < h:
    j = 0
    while j < w:
        ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
        j += 1
    i += 1

'''
for i in range(h):
    for j in range(w):
        ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)
'''
print(ans)