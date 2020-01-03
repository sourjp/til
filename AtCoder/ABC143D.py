n = int(input())
ll = list(map(int, input().split()))
from bisect import bisect_left

def binary_search(arr, low, high, x):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x: low = mid+1
        else: high = mid

    return low


def rec_binary_search(arr, l, r, x):
    if r-l <= 0:
        return l
    
    else:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
    
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)

        else:
            return binary_search(arr, mid+1, r, x)

ll.sort()
ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        c = ll[i] + ll[j]
        limit = bisect_left(ll, c)
        ans += limit - j - 1

print(ans)