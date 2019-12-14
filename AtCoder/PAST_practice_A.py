peoples, train_fee, taxi_fee = map(int, input().split())

ans = min(peoples * train_fee, taxi_fee)

print(ans)
