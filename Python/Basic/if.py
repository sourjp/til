switch = 0

if switch == 0:
    print('if')
elif switch == 1:
    print('elif1')
elif switch == 2:
    print('elif2')
else: 
    print('else')

# A in, not in B ,,, AがBの中にあるかどうかを確認

# Ais, is not B ,,,  AとBのオブジェクトを比較。値ではない。


# all(全てがTrue), any(少なくとも一つがTrue)
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")