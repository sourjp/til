N, M = map(int, input().split())

students = []
for i in range(N):
    students.append(input().split())

checkpoints = []
for i in range(M):
    checkpoints.append(input().split())

for x1, y1 in students:
    result = 99999999999
    index = 1
    for x2, y2 in checkpoints:
        val = abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
        if result > val:
            ans = index
            result = val
        index += 1
    print(ans)