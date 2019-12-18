def func1(arr):
    row_zero = False
    col_zero = False

    for i in range(len(arr)):
        if arr[i][0] == 0:
            row_zero = True

    for j in range(len(arr[0])):
        if arr[0][j] == 0:
            col_zero = True

    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            if arr[i][j] == 0:
                arr[0][j] = 0
                arr[i][0] = 0

    for i in range(len(arr)):
        if arr[i][0] == 0:
            for k in range(len(arr[0])):
                arr[i][k] = 0
            
    for j in range(len(arr[0])):
        if arr[0][j] == 0:
            for k in range(len(arr)):
                arr[k][j] = 0

    if row_zero:
        for i in range(len(arr)):
            arr[i][0] = 0

    if col_zero:
        for j in range(len(arr[0])):
            arr[0][j] = 0

    return arr

arr = [[1, 0, 3, 4, 2], [0, 6, 7, 8, 4], [9, 10, 11, 12, 1], [13, 14, 15, 0, 2]]
print(func1(arr))