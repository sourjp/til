'''
- INPUT:
6
5 2 4 6 1 3

- OUTPUT:
['2', '5', '4', '6', '1', '3']
['2', '4', '5', '6', '1', '3']
['2', '4', '5', '6', '1', '3']
['1', '2', '4', '5', '6', '3']
['1', '2', '3', '4', '5', '6']

'''
n = int(input())
l = list(input().split())

i = 1
j = 0

while i < n:
    while j < i:
        if l[i] < l[j]:
            v = l[i]
            del l[i]
            l.insert(j, v)
            break
        j += 1
    j = 0
    i += 1
    print(l)

'''
number_of_words = int(input())
list_data = list(input().split())

base_count = 0
sort_count = 0

while base_count < number_of_words:
    while sort_count < number_of_words:
        if list_data[base_count] <= list_data[sort_count]:
            tmp_value = list_data[base_count]
            del list_data[base_count]
            list_data.insert(sort_count, tmp_value)
            break
        sort_count += 1
    sort_count = 0
    base_count += 1
    print(list_data)

'''