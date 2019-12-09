n = int(input())
a_list = [int(i) for i in input().split()]
divide = 10 ** 9 + 7

inf=float("inf")
dp=[[inf for i in range(n+1)] for j in range(n+1)]

sum = 0
for i in range(n):
    for j in range(i+1, n):
        if dp[i][j] != inf or dp[j][i] != inf:
            sum += dp[i][j]
            print('yes')
        else:
            val =  a_list[i] ^ a_list[j]
            dp[i][j] = val
            dp[j][i] = val
            sum += val

print(sum % divide)