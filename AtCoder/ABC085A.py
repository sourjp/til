n = int(input())
input_list = list(sorted([int(input()) for _ in range(n)]))

count = 1
for i in range(n-1):
    if input_list[i] < input_list[i+1]:
        count += 1

print(count)


'''
n = int(input())
input_list = set(sorted([int(input()) for _ in range(n)]))
print(len(input_list))
'''