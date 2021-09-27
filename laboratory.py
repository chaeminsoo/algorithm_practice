from itertools import combinations

n,m = map(int,input().split())

field = []
zeros = []

def fast_copy(list):
    return [i[:] for i in list]

for i in range(n):
    row = list(map(int,input().split()))
    for j in row:
        if j == 0:
            zeros.append([i,j])
    field.append(row)

standard_field = fast_copy(field)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def virus_diffusion(x,y):
    if field[x][y] == 2:
        for i in range(4):  
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if field[nx][ny] == 0:
                    field[nx][ny] = 2
                    virus_diffusion(nx,ny)

result = 0
new_walls = list(combinations(zeros,3))

def solution(field):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                cnt += 1
    return cnt

while new_walls:
    case = new_walls.pop()

    for k in case:
        field[k[0]][k[1]] = 1

    for i in range(n):
        for j in range(m):
            virus_diffusion(i,j)

    result = max(result,solution(field))
    print(result)

    field = fast_copy(standard_field)

print(result)