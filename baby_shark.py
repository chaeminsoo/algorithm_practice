from collections import deque

n = int(input())
fish = []
for _ in range(n):
    fish.append(list(map(int,input().split())))

def moving(fish,shark,target,lv):
    x,y = target
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
                if fish[nr][nc] <= lv:
                    q.append((nr,nc))
                    if moving_field[nr][nc] == 0:
                        moving_field[nr][nc] = v+1
                    else:
                        moving_field[nr][nc] = min(v+1,moving_field[nr][nc])
    return moving_field[x][y]

def find_fish(fish,lv,shark):
    ref_dist = 1000
    r = c = 30
    for i in range(n):
        for j in range(n):
            if fish[i][j] != 0 and fish[i][j] < lv:
                dist = moving(fish,shark,(i,j),lv)
                if ref_dist > dist:
                    ref_dist = dist
                    r = i
                    c = j
    if r != 30:
        return (r,c),ref_dist
    else:
        return False,0

for i in range(n):
    for j in range(n):
        if fish[i][j] == 9:
            fish[i][j] = 0
            break
shark = (i,j)

fish_cnt = 0
lv = 2
time_take = 0
target,dist = find_fish(fish,lv,shark)

while target:
    time_take += dist
    r,c = target
    fish[r][c] = 0
    shark = target
    fish_cnt += 1

    if fish_cnt == lv:
        lv += 1
        fish_cnt = 0

    target,dist = find_fish(fish,lv,shark)

print(time_take)