n = int(input())
a = [0] + list(map(int, input().split())) + [0]

cost = 0
for i in range(n+2):
    cost += (abs(a[i] - a[i-1]))

for i in range(1, n+1):
    print(cost + abs(a[i-1]-a[i+1]) - (abs(a[i-1]-a[i]) + abs(a[i]-a[i+1])))