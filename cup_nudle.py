import heapq
import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    d,p = map(int,input().split())
    data.append((d,p))

data.sort()
heap = []
heap_len = 0
ans = 0
for i in data:
    deadline, nudle = i
    
    heapq.heappush(heap,nudle)
    ans += nudle
    heap_len += 1
    if deadline < heap_len:
        ref = heapq.heappop(heap)
        ans -= ref
        heap_len -= 1
print(ans)