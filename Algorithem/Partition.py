'''
計算量はO(n)

- INPUT:
12
13 19 9 5 12 8 7 4 21 2 6 11

- OUTPUT:
[9, 5, 8, 7, 4, 2, 6, '[11]', 21, 13, 19, 12]

'''
num = int(input())
input_list = [int(i) for i in input().split()]

def partition(input_list, threshold):
    boarder_index = 0
    check_index = 0

    while check_index < num:
        if threshold < input_list[check_index]:
            pass
        elif threshold > input_list[check_index]:
            input_list[boarder_index], input_list[check_index] = input_list[check_index], input_list[boarder_index]
            boarder_index += 1            
        check_index += 1

    input_list[-1] = '[' + str(input_list[-1]) + ']'
    input_list[boarder_index], input_list[-1] = input_list[-1], input_list[boarder_index]    

if __name__ == '__main__':
    partition(input_list, input_list[num - 1])
    print(input_list)

