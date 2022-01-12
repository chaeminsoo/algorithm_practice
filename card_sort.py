import heapq

n = int(input())

#heap
heap=[]
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) >1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    ref = one + two
    result+=ref
    heapq.heappush(heap,ref)

print(result)