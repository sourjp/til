import math
N = int(input())

if N%2 != 0:
  answer = 0
else:
  answer = 0
  m = 1
  while int(N//(2*5**m))> 0:
    answer += int(N//(2*5**m))
    m += 1 
print(answer)
