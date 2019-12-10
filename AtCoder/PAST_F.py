s_num = int(input())


word2num_list = []
for i in range(s_num):
    word2num = 0
    for j in input():
        word2num += ord(j)
    word2num_list.append(word2num)

print(word2num_list)
    
