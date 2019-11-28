def count(words):
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

def even_number(count_dict):
    for key in count_dict:
        if count_dict[key] % 2 != 0:
            return('No')
    return('Yes')

if __name__ == '__main__':
    words = input()
    count_dict = {}

    count(words)
    ans = even_number(count_dict)
    print(ans)