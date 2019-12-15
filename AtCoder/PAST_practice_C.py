number, time_limit = map(int, input().split())

def checker(number):
    ans = 1001
    for _ in range(number):
        cost, time = map(int, input().split())
        if time <= time_limit:
            ans = min(ans, cost)

    if ans == 1001:
        return 'TLE'
    else:
        return ans

ans = checker(number)
print(ans)