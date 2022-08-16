# 2873
r,c = map(int,input().split())
board = []
for _ in range(r):
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
dr = ['U','D','L','R']

big_joy = 0
rt = ''
def dfs(now,visited,route,joy):
    global big_joy, rt
    if now == [r-1,c-1]:
        if joy > big_joy:
            big_joy = joy
            rt = route
        return

    x,y = now
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs([nx,ny],visited,route+dr[i],joy+board[nx][ny])
            visited[nx][ny] = False

visited = [[False]*c for _ in range(r)]
visited[0][0] = True
dfs([0,0],visited,'',board[0][0])
print(rt)