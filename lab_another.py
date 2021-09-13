n,m = map(int,input().split())
field = []

for i in range(n):
    field.append(list(map(int,input().split())))

ref_field = [0*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def virus(x,y):
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if ref_field[nx][ny] == 0:
                ref_field[nx][ny] = 2
                virus(nx,ny)

def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ref_field[i][j] == 0:
                cnt +=1
    return cnt

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            
