n, m, k = map(int,input().split())
shark_where = [0]*(m+1)
shark_direction = [0]*(m+1)
shark_cnt = m

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

def spray_smell(shark_where):
    for i in range(1,m+1):
        if shark_where[i] == 0:
            continue
        r,c = shark_where[i]
        smell_field[r][c] = [i,k]

def shark_check(r,c,i,shark_cnt):
    if shark_field[r][c] != 0:
        ref = shark_field[r][c]
        if ref < i:
            shark_where[i] = 0
            shark_cnt -= 1
        else:
            shark_field[r][c] = i
            shark_where[ref] = 0
            shark_cnt -= 1
    else:
        shark_field[r][c] = i
        
def shark_move(shark_where,shark_cnt):
    for i in range(1,m+1):
        if shark_where[i] == 0:
            continue
        r,c = shark_where[i]
        now_direct = shark_direction[i]
        nxt_direct = shark_prefer[i][now_direct]
        for nxt in nxt_direct:
            nr = r + dr[nxt-1]
            nc = c + dc[nxt-1]
            if nr >=0 and nr < n and nc >=0 and nc <n:
                if smell_field[nr][nc] ==0:
                    shark_check(nr,nc,i,shark_cnt)
                else:
                    if smell_field[nr][nc][0] != i:
                        continue
                    else:
                        shark_check(nr,nc,i,shark_cnt)

def remove_smell():
    for i in range(n):
        for j in range(n):
            if smell_field[i][j] == 0:
                continue
            else:
                smell_field[i][j][1] -= 1
                if smell_field[i][j][1] == 0:
                    smell_field[i][j] = 0

time_cnt = 0
spray_smell(shark_where)
while time_cnt < 1000:
    remove_smell()
    shark_move(shark_where,m)
    spray_smell(shark_where)
    time_cnt += 1
    if shark_cnt == 1:
        break

if shark_cnt != 1:
    print(shark_cnt)
    print(-1)
else:
    print(time_cnt)