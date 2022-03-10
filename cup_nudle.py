#1781
import heapq

n = int(input())
data = []
for _ in range(n):
    d,p = map(int,input().split())
    data.append((d,p))

data.sort()
heap = []
for i in data:
    deadline, nudle = i
    
    heapq.heappush(heap,nudle)
    if deadline < len(heap):
        heapq.heappop(heap)
    print(heap)
print(sum(heap))