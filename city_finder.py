from collections import deque

n, m, k, x = map(int,input().split())
inf = float('inf')
roads = [[] for _ in range(n+1)]
result=False
q = deque()
from_x_distance = [inf for _ in range(n+1)]
from_x_distance[x] = 0

for _ in range(m):
    a,b  = map(int,input().split())
    roads[a].append(b)
    if a == x:
        from_x_distance[b] = 1
        q.append(b)

check = [0 for _ in range(n+1)]
check[x] = 1
while q:
    ref_sp  = q.popleft()
    if check[ref_sp] == 0:
        for i in roads[ref_sp]:
            from_x_distance[i] = min(from_x_distance[i],from_x_distance[ref_sp]+1)
            q.append(i)
            check[ref_sp] = 1

for j in range(len(from_x_distance)):
    if from_x_distance[j] == k:
        print(j)
        result = True

if result == False:
    print(-1)