N = int(input())

devide = 10 ** 9 + 7
power = 1

for i in range(1, N + 1):
    power = power * i % devide

print(power)