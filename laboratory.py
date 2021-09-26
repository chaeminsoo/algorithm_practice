from itertools import combinations

n,m = map(int,input().split())

field = []
zeros = []
viruses = []

for i in range(n):
    row = list(map(int,input().split()))
    for j in row:
        if j == 0:
            zeros.append([i,j])
        if j == 2:
            viruses.append([i,j])
    field.append(row)

standard_field = field[:]
standard_viruses = viruses[:]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def virus_diffusion(viruses):
    global dx, dy, field

    try:
        virus = viruses.pop()    
    except IndexError:
        return

    vr = virus[0]
    vc = virus[1]
    
    for i in range(4):
        r = vr + dy[i]
        c = vc + dx[i]

        if r >= 0 and r < n and c >= 0 and c < m:
            if field[r][c] == 0:
                field[r][c] = 2
                viruses.append([r,c])
    virus_diffusion(viruses)

result = 0
new_walls = list(combinations(zeros,3))

def solution():
    global field
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
        
    virus_diffusion(viruses)
    
    result = max(result,solution())

    field = standard_field[:]
    viruses = standard_viruses[:]

print(result)