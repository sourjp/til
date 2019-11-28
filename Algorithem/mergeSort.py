'''
- INPUT:
10
8 5 9 2 6 3 7 1 10 4

- OUTPUT:
left: 0 mid: 1 right: 2
[8, 1000000000] [5, 1000000000]
[5, 8, 9, 2, 6, 3, 7, 1, 10, 4]
left: 0 mid: 2 right: 3
[5, 8, 1000000000] [9, 1000000000]
[5, 8, 9, 2, 6, 3, 7, 1, 10, 4]
left: 3 mid: 4 right: 5
[2, 1000000000] [6, 1000000000]
[5, 8, 9, 2, 6, 3, 7, 1, 10, 4]
left: 0 mid: 3 right: 5
[5, 8, 9, 1000000000] [2, 6, 1000000000]
[2, 5, 6, 8, 9, 3, 7, 1, 10, 4]
left: 5 mid: 6 right: 7
[3, 1000000000] [7, 1000000000]
[2, 5, 6, 8, 9, 3, 7, 1, 10, 4]
left: 5 mid: 7 right: 8
[3, 7, 1000000000] [1, 1000000000]
[2, 5, 6, 8, 9, 1, 3, 7, 10, 4]
left: 8 mid: 9 right: 10
[10, 1000000000] [4, 1000000000]
[2, 5, 6, 8, 9, 1, 3, 7, 4, 10]
left: 5 mid: 8 right: 10
[1, 3, 7, 1000000000] [4, 10, 1000000000]
[2, 5, 6, 8, 9, 1, 3, 4, 7, 10]
left: 0 mid: 5 right: 10
[2, 5, 6, 8, 9, 1000000000] [1, 3, 4, 7, 10, 1000000000]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



devide：
    二分割の再帰関数を実現
merge：
    二分割の限界までいったら、戻りながらソート
    ソートにあたっては最後に番兵を入れて、実際の値を最小値から出し切る
    ソート結果はargs_listに戻すが、rangeはlow, mid, highを渡して維持する
    再帰関数で mid+1, right+1 などはindexとスライスの値のずれを補正するため

'''

N = int(input())
args_list = [ int(_) for _ in input().split()]

left = 0
right = len(args_list) - 1

def devide(args_list, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    devide(args_list, left, mid)
    devide(args_list, mid+1, right)
    merge(args_list, left, mid+1, right+1)

def merge(args_list, left, mid, right):
    print('left:',left, 'mid:', mid, 'right:', right)
    L = args_list[left:mid]
    R = args_list[mid:right]
    L.append(10**9)
    R.append(10**9)

    i, j = 0, 0
    while left < right:
        if L[i] < R[j]:
            args_list[left] = L[i]
            i += 1
        else:
            args_list[left] = R[j]
            j += 1
        left += 1
    print(L, R)
    print(args_list)

if __name__ == '__main__':
    devide(args_list, left, right)

