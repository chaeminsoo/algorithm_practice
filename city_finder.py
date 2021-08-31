from collections import deque

n, m, k, x = map(int,input().split())

roads = []
result =[]
q = deque()
from_x_distance = [0 for _ in range(n+1)]

for _ in range(m):
    a,b  = map(int,input().split())
    roads.append([a,b])
    if a == x:
        from_x_distance[b] = 1
        q.append((b,1))

#----------------
ref_sp = q.popleft()
for i in roads:
    if i[0] == ref_sp[0]:
        q.append((i[1],ref_sp[1]+1))
        from_x_distance[i[1]], 