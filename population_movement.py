n,L,R = map(int,input().split())

N = n*n
cnt = 0
nations=[]
for _ in range(n):
    nations.append(list(map(int,input().split())))

visit = [[0]*n for _ in range(n)]

def fast_copy(list):
    return [i[:] for i in list]

standard_v = fast_copy(visit)

def give_not_visit(visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                return [i,j]

stack=[]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def make_un(stack):
    try:
        coordinate = stack.pop()
    except IndexError:
        return 

    union.append(coordinate)
    r = coordinate[0]
    c = coordinate[1]
    visit[r][c] = 1

    standard = nations[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            ref = nations[nr][nc]
            diff = abs(standard-ref)

            if diff >= L and diff <= R:
                if visit[nr][nc] != 1:
                    stack.append([nr,nc])

    make_un(stack)
    
def move(gou):
    for uns in gou:
        len_uns = len(uns)
        total = 0

        for con in uns:
            total += nations[con[0]][con[1]]

        res = total // len_uns

        for con in uns:
            nations[con[0]][con[1]] = res

while True:
    gou = []

    while True:
        union=[]
        
        coordin = give_not_visit(visit)
        if coordin == None:
            break
        else:
            stack.append(coordin)
            make_un(stack)

            gou.append(union)

    if len(gou) == N:
        break

    move(gou)

    cnt +=1
    visit = fast_copy(standard_v)

print(cnt)

# def a():
#     n = random.randint(1,5)
#     l = random.randint(1,100)
#     r = random.randint(1,100)
#     list = [[] for _ in range(n)]
#     for i in range(n):
#             for j in range(n):
#                     list[i].append(random.randint(0,100))
#     print(n,l,r)
#     for k in range(n):
#             print(list[k])