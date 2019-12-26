n, q = map(int, input().split())

word = input()

counter = [0] * n

for i in range(1, len(word)):
    counter[i] = counter[i-1]
    if word[i-1] + word[i] == 'AC':
        counter[i] += 1

for i in range(q):
    start, end = map(int, input().split())
    print(counter[end-1] - counter[start-1])
