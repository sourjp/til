r1, c1, r2, c2 = map(int, input().split())
mod = 10**9+7

def np(m, n):
    count = [[0 for _ in range(m)] for _ in range(n)] 
    #print(count)

    for i in range(n): 
        count[i][0] = 1

    for j in range(m): 
        count[0][j] = 1
    
    for i in range(1, n): 
        for j in range(m):      
            count[i][j] = count[i-1][j] + count[i][j-1]
    #print(count)
 
    return (count[n-1][m-1])%mod

count = [[0 for _ in range(r2+1)] for _ in range(c2+1)] 
def np2(count):
    for i in range(c2+1): 
        count[i][0] = 1

    for j in range(r2+1): 
        count[0][j] = 1
    
    for i in range(1, c2+1): 
        for j in range(r2+1):      
            count[i][j] = count[i-1][j] + count[i][j-1]

np2(count)
print(count)
print(count[c1][r1] + count[c1][r2] + count[c2][r1] + count[c2][r2])