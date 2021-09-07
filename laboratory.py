from collections import deque
from itertools import combinations

n,m = map(int,input().split())

field = []
zeros=[]
viruses = deque()
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 0:
            zeros.append([i,j])
        elif row[j] == 2:
            viruses.append([i,j])
    field.append(row)
# 4-way
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def virus_diffusion(field,viruses,dx,dy):
    try:
        virus = viruses.popleft()
    except IndexError:
        return
    
    for i in range(4):
        r = virus[0] + dy[i]
        c = virus[1] + dx[i]

        if r < 0 or c < 0 or r > n or c > m:
            continue
        try:
            if field[r][c] == 0:
                field[r][c] = 2
                viruses.append([r,c])
            else:
                continue
        except IndexError:
            continue
    
    virus_diffusion(field,viruses,dx,dy)

result = 0
new_walls = list(combinations(zeros,3))
#---------------- repeat
# for case in new_walls:
#     cnt = 0
#     for k in case:
#         field[k[0]][k[1]] = 1
    
    # virus diffusion
    # virus_diffusion(field,viruses,dx,dy)
    
    # check safe-zone
    # for i in range(n):
    #     for j in range(m):
    #         if field[i][j] == 0:
    #             cnt+=1
    # result = max(result,cnt)

# print(new_walls) # fail reuslt = 0
#----------------------------------------------------------
while new_walls:
    case = new_walls.pop()
    cnt = 0
    for location in case:
        field[location[0]][location[1]] = 1
    
    virus_diffusion(field,viruses,dx,dy)

    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                cnt +=1
    
    result = max(result,cnt)
    break

print(field)
print(result)

#----------------------------------------------------------
if ([0,1],[1,0],[3,4]) in new_walls:
    print(1)
else:
    print(0)
#-------------------------------------------
