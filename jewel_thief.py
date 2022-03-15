# 1202
import sys
import heapq
from bisect import bisect_left

input = sys.stdin.readline
n,k = map(int,input().split())

jewel = []
bag = []
for _ in range(n):
    m,v = map(int,input().split())
    heapq.heappush(jewel,(-v,m,v))
    # jewel.append((m,v))
for _ in range(k):
    c = int(input())
    bag.append(c)
    
def find_bag(target,bag):
    if target > bag[-1]:
        return False
    del bag[bisect_left(bag,target)]
    return True

# jewel.sort(key= lambda x:(-x[1]))
bag.sort()
ans = 0
# for weight, val in jewel:
while jewel:
    if k == 0: break
    ref, weight, val = heapq.heappop(jewel)
    if find_bag(weight,bag):
        ans+=val
        k-=1
    else:
        continue

print(ans)