from itertools import combinations

n,m = map(int,input().split())

field = []
zeros = []
for i in range(n):
    row = list(map(int,input().split()))
    for j in row:
        if j == 0:
            zeros.append([i,j])
    field.append(row)

standard_field = field[:]
lz = len(zeros)

dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

def virus_diffusion(x,y):
    global dx, dy, field,cnt

    if field[x][y] == 2:
        for i in range(4):
            r = x + dy[i]
            c = y + dx[i]

            if r >= 0 and r < n and c >= 0 and c < m:
                if field[r][c] == 0:
                    field[r][c] = 2
                    cnt += 1

result = 0
new_walls = list(combinations(zeros,3))

def solution(new_walls,field):
    global result
    case = new_walls.pop()

    for k in case:
        field[k[0]][k[1]] = 1
    
    for i in range(n):
        for j in range(m):
            virus_diffusion(i,j)
    
    result = max(result,lz - cnt)

while new_walls:
    solution(new_walls,field)

    field = standard_field[:]
    cnt = 0

print(result)