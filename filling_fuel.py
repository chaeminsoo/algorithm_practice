#1826
from bisect import bisect_left
import heapq

n = int(input())
gas_station = []
for _ in range(n):
    a,b = map(int,input().split())
    gas_station.append((a,b))
needed_gas, now_gas= map(int,input().split())
gas_station.sort()

pre_cursor_ = 0
now_cursor_ = now_gas
heap = []
cnt = 0

while True:
    for i in gas_station[bisect_left(gas_station,(pre_cursor_,101)):bisect_left(gas_station,(now_cursor_,101))]:
        heapq.heappush(heap,(-i[1],i[1]))
    if now_cursor_ < needed_gas:
        pre_cursor_ = now_cursor_
        try:
            now_cursor_ += heapq.heappop(heap)[1]
            cnt += 1
        except IndexError:
            cnt = -1
            break
        continue
    else:
        break
    
print(cnt)