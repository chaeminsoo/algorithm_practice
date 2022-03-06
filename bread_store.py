r,c = map(int,input().split())
field = []
for _ in range(r):
    data = list(input())
    field.append(data)
visit = [[False]*c for _ in range(r)]

dr = [-1,0,1]
dc = [1,1,1]

def install_pipe(x,y):
    if y == c-1:
        return True
    
    for i in range(3):
        nr = x + dr[i]
        nc = y + dc[i]

        if nr >= 0 and nr < r and nc >=0 and nc < c:
            if field[nr][nc] =='.' and visit[nr][nc] == False:
                visit[nr][nc] = True
                if install_pipe(nr,nc):
                    return True
    return False
cnt = 0
for i in range(r):
    if install_pipe(i,0):
        cnt +=1
print(cnt)