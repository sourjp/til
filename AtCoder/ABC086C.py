n = int(input())
travel_list = [[0, 0, 0]]

for _ in range(n):
    travel_list.append(list(map(int, input().split())))

complete = True
for i in range(n):
    time = travel_list[i+1][0] - travel_list[i][0]
    x_distance =  abs(travel_list[i+1][1] - travel_list[i][1])
    y_distance =  abs(travel_list[i+1][2] - travel_list[i][2])
    xy_distance = x_distance + y_distance

    if time >= xy_distance:
        if time % 2 != xy_distance % 2:
            complete = False
            break
    else:
        complete = False
        break       

print('Yes' if complete else 'No')