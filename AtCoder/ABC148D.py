n = int(input())
input_list = list(map(int, input().split()))

i = 0
c = 1
cnt = 0
while i < n:
    if input_list[i] == c:   
        c += 1
    else:
        cnt += 1     
        
    i += 1

print(cnt if c > 1 else '-1')