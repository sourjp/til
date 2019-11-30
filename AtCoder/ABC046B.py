ball, color = map(int, input().split())

first = color * 1
second = 1
if ball != 1: second = (color - 1) ** (ball-1)

print(first * second)