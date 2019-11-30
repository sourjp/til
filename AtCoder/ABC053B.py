s = input()

found_a = False
high = 0
low = 0

for index, word in enumerate(s):
    if found_a == False:
        if word == 'A':
            low = index
            found_a = True
    if word == 'Z':
        high = index

print(high - low + 1)