import heapq

t = int(input())
INF = 1e9
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def solution(n,graph):
    distance = [[INF]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    distance[0][0] = graph[0][0]
    visited[0][0] = True
    q=[]
    heapq.heappush(q,[graph[0][0],0,0])
    while q:
        v,r,c = heapq.heappop(q)
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nc >= 0 and nr < n and nc < n:
                if visited[nr][nc] == False:
                    new_dis = graph[nr][nc] + v
                    if new_dis < distance[nr][nc]:
                        distance[nr][nc] = new_dis
                        heapq.heappush(q,[new_dis,nr,nc])

    return distance[n-1][n-1]

answer=[]
for _ in range(t):
    n = int(input())
    field = []
    for _ in range(n):
        field.append(list(map(int,input().split())))
    answer.append(solution(n,field))

for i in answer:
    print(i)