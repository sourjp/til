'''
そもそも文字列とは何か？
ASCII
    7桁の二進数。つまり128文字。アルファベット系列のみ。

UNICODE
    アルファベットだけでは足りない国（日本とか）では、128bitじゃ文字が表現できない
    なので2byte, 4byteなど各国で仕組みが乱立したので、世界標準として作られた。

1. Dyanmic Programing
    突合をするので追加のメモリが必要
    ただ入力の順番を変える必要はない
    文字なら文字コードで範囲が決まっているので、
    そこをcheckしてboolで履歴を作ればいい

2. Sort
    sortはO(logn)で実施できる
    そのあと重複がないのであれば前後の文字は必ず同一ではないのでO(n)で処理できる

'''
test = [
    'tenis',
    'aiueoa',
    'ああ',
    'sエス',
    '12359',
    '明日',
    'golf',
]
# set the input


def check_dp_ascii(words):
    dp_ascii = ['' for i in range(129)]

    for word in words:
        if ord(word) > 128:
            return 'BAD: {} is not ASCII word'.format(words)
        ascii_num = ord(word)
        if dp_ascii[ascii_num] == True:
            return 'BAD: {} have one more same word'.format(words)

        dp_ascii[ascii_num] = True
    return 'GOOD: {} have no one more word'.format(words)


def check_dp_unicode(words):
    dp_ascii = ['' for i in range(8**8)]

    for word in words:
        if ord(word) > 8**8:
            return 'BAD: {} is not UTF-8 word'.format(words)
        ascii_num = ord(word)
        if dp_ascii[ascii_num] == True:
            return 'BAD: {} have one more same word'.format(words)

        dp_ascii[ascii_num] = True
    return 'GOOD: {} have no one more word'.format(words)



if __name__ == "__main__":
    for w in test:
        print(check_dp_ascii(w))
        print(check_dp_unicode(w))
        print('---')

