N, K, X, Y = map(int, open(0).read().split())

before_fee = 0
after_fee = 0

if N >= K:
    before_fee = K * X
    if N > K:
        after_fee = (N-K) * Y
else: 
    before_fee = N * X

print(before_fee + after_fee)