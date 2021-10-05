from itertools import combinations

n = int(input())

answer = False
result = False

field =[]
blanks = []
teachers = []

for i in range(n):
    row = list(input().split())
    for j in range(n):
        if row[j] == 'X':
            blanks.append([i,j])
        elif row[j] == 'T':
            teachers.append([i,j])
    field.append(row)

standard_field = [i[:] for i in field]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def check(teacher):
    global dr,dc,field,n,unable,result,mul
    
    if unable == [1,1,1,1]:
        return
        
    r=teacher[0]
    c=teacher[1]
    
    for i in range(4):
        if unable[i] == 1:
            continue

        nr = r + (dr[i]*mul)
        nc = c + (dc[i]*mul)

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            unable[i] = 1
            continue
        
        if field[nr][nc] == 'S':
            result = True
            return
        elif field[nr][nc] == 'O' or field[nr][nc] == 'T':
            unable[i] = 1
        
    mul +=1
    check(teacher)
    
unable = [0,0,0,0]
mul = 1

obj_cases = list(combinations(blanks,3))
case_num = len(obj_cases)
cnt = 0

while obj_cases:
    case = obj_cases.pop()

    for i in case:
        field[i[0]][i[1]] = 'O'

    for teacher in teachers:
        check(teacher)
        if result:
            break
        mul = 1
        unable = [0,0,0,0]
    
    if result:
        mul = 1
        unable = [0,0,0,0]
        field  = [i[:] for i in standard_field]
        result = False
    else:
        answer = True
        break
    
if answer:
    print('YES')
else:
    print('NO')