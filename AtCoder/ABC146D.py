n = int(input())
graph = [[] for _ in range(n+1)]

for index, _ in enumerate(range(n-1)):
    a, b = map(int, input().split())
    graph[a-1].append([b-1, index])


ans = [None] * (n-1)

def paint(curr_v, parent_color):
    child_color = 1
    for next_v, index in graph[curr_v]:
        # if child_color same as parent_color, then child_color has count up.
        if child_color == parent_color:
            child_color += 1


        ans[index] = child_color

        # child_color will be parent_color for next child.
        paint(next_v, child_color) 
        child_color += 1

# start root node
paint(0, 0) 
print(max(ans))
print(*ans, end='\n')