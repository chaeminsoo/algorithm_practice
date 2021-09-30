from itertools import combinations

n = int(input())

answer = False

field =[]
blanks = []
teachers = []
students = []

for i in range(n):
    row = list(input().split())
    for j in range(n):
        if row[j] == 'X':
            blanks.append([i,j])
        elif row[j] == 'T':
            teachers.append([i,j])
        elif row[j] == 'S':
            students.append([i,j])
    field.append(row)

standard_field = [i[:] for i in field]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def check(field):
    global teachers, students,t_cnt,unable,mul
    try:
        now_t = teachers[t_cnt]
        r=now_t[0]
        c=now_t[1]
    except IndexError:
        return
    
    for i in range(4):
        if unable[i] == 1:
            continue

        nr = r + (dr[i]*mul)
        nc = c + (dc[i]*mul)

        if field[nr][nc] == 'S':
            return True
        elif field[nr][nc] == 'O' or nr < 0 or nc < 0 or nr > n or nc > n:
            unable[i] = 1
    
    t_cnt +=1
    mul +=1
    
    check(field)

obj_cases = list(combinations(blanks,3))

while obj_cases:
    case = obj_cases.pop()

    for i in case:
        field[i[0]][i[1]] = 'O'

    t_cnt = 0
    mul = 1
    unable = [0,0,0,0]

    check(field)
    
    if answer:
        break
    else:
        field  = [i[:] for i in standard_field]
    
if answer:
    print('NO')
else:
    print('YES')