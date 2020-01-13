n, k, m = map(int, input().split())
points = list(map(int, input().split()))

psum = sum(points)

if n*m <= psum:
    print('0')

elif n * m - psum <= k:
    print(n * m - psum)

else:
    print('-1')
