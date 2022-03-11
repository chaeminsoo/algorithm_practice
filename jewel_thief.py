# 1202
from bisect import bisect_left
import sys

input = sys.stdin.readline
n,k = map(int,input().split())

jewel = []
bag = []
for _ in range(n):
    m,v = map(int,input().split())
    jewel.append((m,v))
for _ in range(k):
    c = int(input())
    bag.append(c)
    
jewel.sort(key= lambda x:(-x[1],x[0]))
bag.sort()
ans = 0
for i in jewel:
    weight, val = i
    idx = bisect_left(bag,weight)
    if idx == k:
        idx-=1
    if k <= 0:
        break
    
    if bag[idx] < weight:
        continue
    else:
        ans+=val
        k-=1
print(ans)