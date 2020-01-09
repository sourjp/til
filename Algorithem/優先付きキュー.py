''' https://github.com/python/cpython/blob/master/Lib/heapq.py
heqap とも言われる

0~30までの配列を与えられた時に次のような順番になるようにツリー構造を作る
この構造の特徴はrootが必ず最小の値になるという構造
それを実現するために必ずchildはparentより値が大きいものにするというアルゴリズムがポイント。
新しい数値が追加されたらリーフとして追加し、parentと比較しながら位置を決定する。
rootがなくなった場合はletf rightを比較して、小さい方をparentにすることを繰り返す。


                                   0
                  1                                 2
          3               4                5               6
      7       8       9       10      11      12      13      14
    15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30

またこれには配列に特徴があり、child indexが必ず 2k + 1 or 2k + 2(k=parent index)で示されることにある。
上の例では0のchildは2 * 0 + 1 = 1と2 * 0 + 2 = 2となる。

'''

import heapq
import random

test = list(range(0, 10))
random.shuffle(test)
print('input list:', test)


heapq.heapify(test)
print('heapq sorted as heapq:', test)
print(heapq.heappop(test))
heapq.heappush(test, 100)
heapq.heappush(test, 5)
heapq.heappush(test, 2)
print('heapq:', test)

'''
Pythonのlibraryでsupportしているのはmin-heapq
max-heapqには次の２種類の方法で実現できる
1. _heapify_max
2. 負数にする

'''

import heapq
import random

test2 = list(range(10))
random.shuffle(test2)

test3 = test2[:]

print(test2)

heapq._heapify_max(test2)
print('sorted max-heap:', test2)

print(heapq._heappop_max(test2))
#今はまだ_heappush_maxはない

print('max-heqp:', test2)
print(heapq._heapreplace_max(test2, 100))
print('max-heqp:', test2)


# 負数にすればmax-heapqと同じになる。ただし切り捨ての計算を入れると、 5 // 2 = 2だが -5 // 2 = -3なので注意。
print(test3)
test3 = [-x for x in test3]

heapq.heapify(test3)
print(test3)

print([-x for x in test3])

