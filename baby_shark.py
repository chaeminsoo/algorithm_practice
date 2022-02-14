from collections import deque

n = int(input())
fish = []
for i in range(n):
    fish.append(list(map(int,input().split())))

def moving(fish,shark):
    moving_field = [[0]*n for _ in range(n)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q = deque()
    q.append(shark)
    while q:
        r,c = q.popleft()
        v = moving_field[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >=0 and nr < n and nc >= 0 and nc < n:
                if fish[nr][nc] <= lv and moving_field[nr][nc] == 0:
                    q.append((nr,nc))
                    moving_field[nr][nc] = v+1
    return moving_field

def find_fish(moving_field):
    ref = []
    for i in range(n):
        for j in range(n):
            if moving_field[i][j] != 0 and fish[i][j] < lv and fish[i][j] != 0:
                ref.append((moving_field[i][j],i,j))
    ref.sort(reverse=True, key= lambda x:(x[0],x[1],x[2]))
    try:
        return ref.pop()
    except IndexError:
        return False

for i in range(n):
    for j in range(n):
        if fish[i][j] == 9:
            fish[i][j] = 0
            shark = (i,j)

fish_cnt = 0
lv = 2
time_take = 0
status = find_fish(moving(fish,shark))
while status:
    t,x,y = status
    time_take += t
    fish[x][y] = 0
    shark = (x,y)
    fish_cnt += 1
    if fish_cnt == lv:
        lv += 1
        fish_cnt = 0
    status = find_fish(moving(fish,shark))

print(time_take)