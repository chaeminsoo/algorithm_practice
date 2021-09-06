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

def virus_diffusion(field,viruses):
    try:
        virus = viruses.popleft()
    except IndexError:
        return

    for i in range(4):
        try:
            new_v_r = virus[0] + dy[i]
            new_v_c = virus[1] + dx[i]
            if field[new_v_r][new_v_c] != 0:
                continue
            else:
                field[new_v_r][new_v_c] = 2
                viruses.append([new_v_r,new_v_c])
        except IndexError:
            continue
    virus_diffusion(field,viruses)

result = 0
new_walls = list(combinations(zeros,3))
#---------------- repeat
# for case in new_walls:
#     cnt = 0
#     for k in case:
#         field[k[0]][k[1]] = 1
    
#     # virus diffusion
#     virus_diffusion(field,viruses)

#     # check safe-zone
#     for i in range(n):
#         for j in range(m):
#             if field[i][j] == 0:
#                 cnt+=1
#     result = max(result,cnt)

# print(result) # fail reuslt = 0


case = new_walls[0]
    
for k in case:
    field[k[0]][k[1]] = 1
virus_diffusion(field,viruses)

print(field)