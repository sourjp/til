import sys

#data = set()
data = []
for i in range(20):
    a = len(data)
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))

#    data.add(i)
    data.append(i)

''' list()
Length:   0; Size in bytes:   72
Length:   1; Size in bytes:  104
Length:   2; Size in bytes:  104
Length:   3; Size in bytes:  104
Length:   4; Size in bytes:  104
Length:   5; Size in bytes:  136
Length:   6; Size in bytes:  136
Length:   7; Size in bytes:  136
Length:   8; Size in bytes:  136
Length:   9; Size in bytes:  200
Length:  10; Size in bytes:  200
Length:  11; Size in bytes:  200
Length:  12; Size in bytes:  200
Length:  13; Size in bytes:  200
Length:  14; Size in bytes:  200
Length:  15; Size in bytes:  200
Length:  16; Size in bytes:  200
Length:  17; Size in bytes:  272
Length:  18; Size in bytes:  272
Length:  19; Size in bytes:  272
'''
''' set()
Length:   0; Size in bytes:  232
Length:   1; Size in bytes:  232
Length:   2; Size in bytes:  232
Length:   3; Size in bytes:  232
Length:   4; Size in bytes:  232
Length:   5; Size in bytes:  744
Length:   6; Size in bytes:  744
Length:   7; Size in bytes:  744
Length:   8; Size in bytes:  744
Length:   9; Size in bytes:  744
Length:  10; Size in bytes:  744
Length:  11; Size in bytes:  744
Length:  12; Size in bytes:  744
Length:  13; Size in bytes:  744
Length:  14; Size in bytes:  744
Length:  15; Size in bytes:  744
Length:  16; Size in bytes:  744
Length:  17; Size in bytes:  744
Length:  18; Size in bytes:  744
Length:  19; Size in bytes: 2280
'''