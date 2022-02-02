n,m = map(int,input().split())
INF = 1e9
graph = [[INF]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

ref = [0]*n

for r in range(n):
    for c in range(n):
        if graph[r][c] != INF:
            ref[r] +=1
            ref[c] +=1
cnt=0
for i in ref:
    if i >n:
        cnt+=1

print(cnt)