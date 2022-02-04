import heapq

n,m = map(int,input().split())
INF = 1e9
graph = [[] for _ in range(n)]
dist = [INF]*n
visited = [False]*n
dist[0] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

q = []
heapq.heappush(q,[0,0])
while q:
    v,idx = heapq.heappop(q)
    visited[idx] = True
    nxt_v = v +1

    for i in graph[idx]:
        if nxt_v < dist[i] and visited[i] == False:
            dist[i] = nxt_v
            heapq.heappush(q,[nxt_v,i])

M = max(dist)
print(dist.index(M)+1,M,dist.count(M))