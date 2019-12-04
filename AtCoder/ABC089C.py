num = int(input())

m = 0
a = 0
r = 0
c = 0
h = 0

P1 = [0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,2]
P2 = [1 ,1 ,1 ,2 ,2 ,3 ,2 ,2 ,3 ,3]
P3 = [2 ,3 ,4 ,3 ,4 ,4 ,3 ,4 ,4 ,4]


for _ in range(num):
    word = input()
    if word[0] == 'M':
        m += 1
    if word[0] == 'A':
        a += 1
    if word[0] == 'R':
        r += 1
    if word[0] == 'C':
        c += 1
    if word[0] == 'H':
        h += 1

D = [m, a, r, c, h]

sum = 0
for d in range(10):
    sum += D[P1[d]] * D[P2[d]] * D[P3[d]]

print(sum)