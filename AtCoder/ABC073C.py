N = int(input())

input_set = set()
for _ in range(N):
    a = int(input())
    if a in input_set:
        input_set.remove(a)        
    else:
        input_set.add(a)
    
print(len(input_set))