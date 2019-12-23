n, k = map(int, input().split())

checker = list(map(str, input().split()))

cont = True
while cont:
    keep = True
    for nn in str(n):
        if nn in checker:
            keep = False
            break
        
    if keep: break
    n += 1

print(n)