def bs(left, right, p, dut):
    while left < right:
        mid = (left+right) // 2
        if dut[mid] == p: break
        if dut[mid] < p: left = mid + 1
        else: right = mid
    return mid


def run(p):
    # get range to temple
    pos = bs(0, A, p, s)
    print('t-p', pos)
    if s[pos] == p: range_to_temple = 0
    else:
        if p-s[pos] < s[pos+1]-p:
            range_to_temple = p-s[pos]
            p -= p-s[pos]
        else:
            range_to_temple = s[pos+1]-p
            p += s[pos+1]-p

    # get range to shrine
    pos = bs(0, B, p, t)
    if t[pos] == p: range_to_shrine = 0
    else: range_to_shrine = min(p-t[pos], t[pos+1]-p)

    print('t:', range_to_temple, 's:', range_to_shrine)
    return abs(range_to_temple) + abs(range_to_shrine)        

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
s.append(float('inf'))
t.append(float('inf'))
for p in x:

    print(run(p))