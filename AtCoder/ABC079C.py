A, B, C, D = map(str, input())

op = ['+', '-']
for op1 in op:
    for op2 in op:
        for op3 in op:
            result = A+op1+B+op2+C+op3+D
            if eval(result) == 7:
                print(result + '=7')
                exit()