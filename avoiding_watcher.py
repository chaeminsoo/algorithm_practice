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
    global dr,dc,field,n,unable,answer,mul
    
    if unable == [1,1,1,1]:
        return

    r=teacher[0]
    c=teacher[1]
    
    for i in range(4):

        nr = r + (dr[i]*mul)
        nc = c + (dc[i]*mul)

        try:
            if field[nr][nc] == 'S':
                answer = True
                return
            elif field[nr][nc] == 'O' or field[nr][nc] == 'T':
                unable[i] = 1
        except IndexError:
            unable[i] = 1
    mul +=1
    check(teacher)
    
unable = [0,0,0,0]
mul = 1

obj_cases = list(combinations(blanks,3))

while obj_cases:
    case = obj_cases.pop()

    for i in case:
        field[i[0]][i[1]] = 'O'

    for teacher in teachers:
        check(teacher)
        if answer == True:
            break
    
    if answer:
        break
    else:
        field  = [i[:] for i in standard_field]
    
if answer:
    print('NO')
else:
    print('YES')