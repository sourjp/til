s = input()
t = input()

def checking(check_dict, key, val, yes_ans):
    if key in check_dict:
        if check_dict[key] == val:
            pass
        else:
            print('No')
            yes_ans = False
            return yes_ans
    else:
        check_dict[key] = val
    return yes_ans


t_dict = {}
s_dict = {}
yes_ans = True

for t_val, s_val in zip(t, s):
    yes_ans = checking(t_dict, t_val, s_val, yes_ans)
    if yes_ans == False:
        break
    yes_ans = checking(s_dict, s_val, t_val, yes_ans)
    if yes_ans == False:
        break

if yes_ans:
    print('Yes')