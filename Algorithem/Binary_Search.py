import random
import bisect

def bs_bool(arr, x, lo=0, hi=None) -> bool:
    if hi == None:
        hi = len(arr)

    while lo < hi:
        mid = (hi + lo) // 2

        if arr[mid] == x: return True
        elif arr[mid] < x: lo = mid+1
        else: hi = mid
    
    return False

def bs_index(arr, x, lo=0, hi=None) -> int:
    if hi == None:
        hi = len(arr)

    while lo < hi:
        mid = (hi + lo) // 2

        if arr[mid] < x: lo = mid+1
        else: hi = mid
    
    return lo

arr = [random.randrange(0, 100) for _ in range(10)]
arr.sort()

x = 30

print(bs_bool(arr, x))
print(bs_index(arr, x))
print(bisect.bisect_left(arr, x))
print(bisect.bisect_right(arr, x))
print(arr)