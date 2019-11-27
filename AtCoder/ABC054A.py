A, B = map(int, input().split())


if A == 1 or B == 1:
    if A == B:
        print('Draw')
    elif A == 1:
        print('Alice')
    elif B == 1:
        print('Bob')
else:
    if A > B:
        print('Alice')
    elif A < B:
        print('Bob')
    else:
        print('Draw')