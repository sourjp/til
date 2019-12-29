x = int(input())

def checker(x):
    found = False
    upper = x ** (1/2)

    for i in range(2, round(upper)):
        if x % i == 0:
            found = True
            break

    return False if found == True else True

x -= 1
ok = False

while not ok:
    x += 1
    ok = checker(x)

print(x)