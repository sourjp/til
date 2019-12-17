l = set([4, 5, 6, 7, 8, 9])
ll = [0, 1, 2, 3, 4, 5]
ll = set(ll)
lll = {1, 2, 3, 4, 5}

print(l, type(l))
print(ll, type(ll))

print(l | ll)   # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 全ての集合和をだす

print(l - ll)   # {8, 9, 6, 7}  集合から集合を引いた結果
print(ll - l)   # {0, 1, 2, 3}

print(l ^ ll)   # {0, 1, 2, 3, 6, 7, 8, 9}  重複していない集合をだす

print(l & ll)   # {4, 5}    重複している集合をだす