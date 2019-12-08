def minimumBribes(q):
    count = 0
    q = [v - 1 for v in q]

    for i, p in enumerate(q):
        if p - i > 2:
            return print('Too chaotic')
        for j in range(max(p - 1, 0), i):
            if q[j] > p:
                count += 1
    return print(count)


t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))
    minimumBribes(q)

