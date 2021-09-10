import copy
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
num_zero = len(zeros)

# 4-way
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def virus_diffusion(field,viruses,dx,dy,zeros):
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
                try:
                    zeros.remove([r,c])
                except ValueError:
                    pass
                viruses.append([r,c])
            else:
                continue
        except IndexError:
            continue
    
    virus_diffusion(field,viruses,dx,dy,zeros)

result = 0
new_walls = list(combinations(zeros,3))

for case in new_walls:
    for wall in case:
        field[wall[0]][wall[1]] = 1
    
    virus_diffusion(field,viruses,dx,dy,zeros)
    
    result = max(result,len(zeros))
    
print(result)