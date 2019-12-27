def pm(input_list):
    calc_result = [0]
    cnt = 0
    
    for i in range(n):
        if i % 2 == 0: plus = True
        else: plus = False

        x = input_list[i] + calc_result[i]
        if plus:
            if x > 0:
                calc_result.append(x)
            
            else:
                cnt += 1 - x
                calc_result.append(1)

        else:
            if x < 0:
                calc_result.append(x)
            
            else:
                cnt += abs(-1 - x)
                calc_result.append(-1)

    return cnt

def mp(input_list):
    calc_result = [0]
    cnt = 0
    
    for i in range(n):
        if i % 2 == 0: minus = True
        else: minus = False

        x = input_list[i] + calc_result[i]
        if minus:
            if x < 0:
                calc_result.append(x)
            
            else:
                cnt += abs(-1 - x)
                calc_result.append(-1)

        else:
            if x > 0:
                calc_result.append(x)
            
            else:
                cnt += 1 - x
                calc_result.append(1)

    return cnt


n = int(input())
input_list = list(map(int, input().split()))

print(min(pm(input_list), mp(input_list)))