import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

nlist = list(range(1, n+1))
nmlist = []

for val in itertools.permutations(nlist, n):
    nmlist.append(val)

print(abs(nmlist.index(p)-nmlist.index(q)))