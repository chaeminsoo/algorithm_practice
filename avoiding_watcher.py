from itertools import combinations

n = int(input())

answer = False

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
    result = False
    mul = 1
    unable = [0,0,0,0]
    
    r=teacher[0]
    c=teacher[1]
    
    while unable == [1,1,1,1]:
        for i in range(4):
            if unable[i] == 1:
                continue

            nr = r + (dr[i]*mul)
            nc = c + (dc[i]*mul)

            if field[nr][nc] == 'S':
                result = True
                return result
            elif field[nr][nc] == 'O' or field[nr][nc] == 'T' or nr < 0 and nr >= n and nc < 0 and nc >= n:
                unable[i] = 1
        mul +=1
    
    return result

obj_cases = list(combinations(blanks,3))

while obj_cases:
    case = obj_cases.pop()

    for i in case:
        field[i[0]][i[1]] = 'O'

    for teacher in teachers:
        if check(teacher):
            answer = True
            break
    
    if answer:
        break
    else:
        field  = [i[:] for i in standard_field]
    
if answer:
    print('NO')
else:
    print('YES')