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
ref_field = copy.deepcopy(field)

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

def check(field):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                cnt +=1
    return cnt

def reset(field):
    field = ref_field[:]
    return field

all_cases = list(combinations(zeros,3))
result = 0
cnt = 0
for case in all_cases:
    for wall in case:
        field[wall[0]][wall[1]] = 1
    print(field)    
    virus_diffusion(field,viruses,dx,dy)
    print(field)    

    result = max(result,check(field))

    field = reset(field)
    print(field)
    cnt+=1
    if cnt == 2:
        break
    # break    

print(result)