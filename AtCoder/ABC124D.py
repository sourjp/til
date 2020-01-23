n, k = map(int, input().split())
s = input()
ss = []

cnt = 0

if s[0] == '0': ss.append(0)
i = 0
while i < n:
    j = i
    while j < n and s[i] == s[j]: j += 1
    ss.append(j-i)
    i = j
if s[-1] == '0': ss.append(0)

right = 2*k+1
left = 0
val = sum(ss[:right])
ans = val

#print(ss)
while right < len(ss):
    for i in [1, 2]:
        #print('for', ss[left], ss[right])
        val += ss[right]
        val -= ss[left]
        left += 1
        right += 1
    #print(left, right, val)
    ans = max(ans, val)
    
print(ans)

'''
n, k = map(int, input().split())
s = input()
ss = []

cnt = 0

if s[0] == '0': ss.append(0)
i = 0
while i < n:
    j = i
    while j < n and s[i] == s[j]: j += 1
    ss.append(j-i)
    i = j
if s[-1] == '0': ss.append(0)

#print(ss)
ans = []
i = 0
while i < n:
    #print(ans, i, sum(ss[i:i+2*k+1]))
    #if i+2*k+1 > n:
    #    break
    ans.append(sum(ss[i:i+2*k+1]))
    i += 2

print(max(ans))
'''
