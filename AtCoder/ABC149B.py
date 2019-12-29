a, b, k = map(int, input().split())

def test(a, b, k):
    if k - a > 0:
        kk = k - a
        return 0, max(0, b - kk)

    else:
        return a-k, b

ans = test(a, b, k)
print(*ans)