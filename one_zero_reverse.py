import math

n = input()

cnt = 0

for i in range(1,len(n)):
    now = n[i-1]
    next = n[i]

    if now == next:
        continue
    else:
        cnt+=1

print(math.ceil(cnt/2))