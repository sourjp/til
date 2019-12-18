def func1(arr):
    n = len(arr)

    layer = 0    
    while layer < n/2:

        first = layer
        last = n - 1 - layer

        i = first
        while i < last:
            offset = i - first
            top = arr[first][i]

            # left to up
            arr[first][i] = arr[last - offset][first]
            print(arr[first][i])
            # down to left
            arr[last - offset][first] = arr[last][last - offset]

            # right to down
            arr[last][last - offset] = arr[i][last]

            # up to right
            arr[i][last] = top
            
            i += 1
            
        layer += 1
    return arr

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(func1(arr))