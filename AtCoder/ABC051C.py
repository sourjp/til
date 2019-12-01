sx, sy, tx, ty = map(int, input().split())

w = tx - sx
h = ty - sy

ans = str()
ans += 'R' * w
ans += 'U' * h
ans += 'L' * w
ans += 'D' * h

ans += 'D'
ans += 'R' * (w + 1)
ans += 'U' * (h + 1)
ans += 'L'

ans += 'U'
ans += 'L' * (w + 1)
ans += 'D' * (h + 1)
ans += 'R'

print(ans)