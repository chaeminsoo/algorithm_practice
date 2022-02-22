n, m, k = map(int,input().split())
shark_where = [0]*(m+1)
shark_direction = [0]*(m+1)

for i in range(n):
    data = list(map(int,input().split()))
    for j, num in enumerate(data):
        if num != 0:
            shark_where[num] = [i,j]

direction_data = list(map(int,input().split()))
for num,d in enumerate(direction_data):
    shark_direction[num+1] = d

shark_prefer = [[0] for _ in range(m+1)]
for i in range(m):
    for j in range(4):
        prefer_data = list(map(int,input().split()))
        shark_prefer[i+1].append(prefer_data)

shark_field = [[0]*n for _ in range(n)]
smell_field = [[0]*n for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def shark_cnt(shark_where):
    cnt = 0
    for i in shark_where:
        if i != 0:
            cnt += 1
    return cnt

def spray_smell(shark_where):
    for i in range(1,m+1):
        if shark_where[i] == 0:
            continue
        r,c = shark_where[i]
        smell_field[r][c] = [i,k]

def shark_check(r,c,shark_num):
    if shark_field[r][c] != 0:
        ref = shark_field[r][c]
        if ref < shark_num:
            shark_where[shark_num] = 0
        else:
            shark_field[r][c] = shark_num
            shark_where[shark_num] = [r,c]
            shark_where[ref] = 0
    else:
        shark_field[r][c] = shark_num
        shark_where[shark_num] = [r,c]
        
def shark_move(shark_where):
    for i in range(1,m+1):
        if shark_where[i] == 0:
            continue
        r,c = shark_where[i]
        now_direct = shark_direction[i]
        nxt_directs = shark_prefer[i][now_direct]
        ref = True
        for nxt in nxt_directs:
            nr = r + dr[nxt-1]
            nc = c + dc[nxt-1]
            if nr >=0 and nr < n and nc >=0 and nc <n:
                if smell_field[nr][nc] ==0:
                    shark_check(nr,nc,i)
                    shark_field[r][c] = 0
                    shark_direction[i] = nxt
                    ref = False
                    break
                else:
                    continue
        
        if ref == True:
            for nxt in nxt_directs:
                nr = r + dr[nxt-1]
                nc = c + dc[nxt-1]
                if nr >=0 and nr < n and nc >=0 and nc <n:
                    if smell_field[nr][nc][0] == i:
                        shark_check(nr,nc,i)
                        shark_field[r][c] = 0
                        shark_direction[i] = nxt
                        break

def remove_smell():
    for i in range(n):
        for j in range(n):
            if smell_field[i][j] == 0:
                continue
            else:
                if shark_field[i][j] !=0:
                    continue
                smell_field[i][j][1] -= 1
                if smell_field[i][j][1] == 0:
                    smell_field[i][j] = 0
                    
time_cnt = 0
spray_smell(shark_where)
while time_cnt < 1000:
    shark_move(shark_where)
    spray_smell(shark_where)
    remove_smell()
    time_cnt += 1
    if shark_cnt(shark_where) == 1:
        break

if shark_cnt(shark_where) != 1:
    print(-1)
else:
    print(time_cnt)