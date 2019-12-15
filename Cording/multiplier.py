
def output(n):
    ''' O(n^4)
    '''
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)
                        break

def output2(n):
    ''' O(n^3)
    '''

    for a in range(n):
        for b in range(n):
            for c in range(n):
                ab = a**3 + b**3 
                d3 = ab - c**3                
                d = d3 ** (1/3)
                cd = c**3 + d**3
                if ab == cd and 0 <= d and d <= n:
                    print(a, b, c, d)

def output3(n):
    ''' O(n^2) + O(n^2 * k) : n < k
    '''
    dp = [[] for i in range(n**3 + n**3)]
    for c in range(n):
        for d in range(n):
            cd = c**3 + d**3
            dp[cd].append([c, d])

    for a in range(n):
        for b in range(n):
            save = []

            ab = a**3 + b**3
            save = dp[ab]

            for save_cd in save:
                c, d = save_cd
                print(a, b, c, d)
    print(dp)


def output4(n):
    ''' O(n^2) + O(n * k^2) : n < k
    '''
    dp = [[] for i in range(n**3 + n**3)]
    for c in range(n):
        for d in range(n):
            cd = c**3 + d**3
            dp[cd].append([c, d])

    for data in dp:
        for pair1 in data:
            for pair2 in data:
                a, b = pair1
                c, d = pair2
                print(a, b, c, d)

n = 500

#output(n)
#output2(n)
#output3(n)
output4(n)