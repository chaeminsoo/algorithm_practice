n,L,R = map(int,input().split())

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

def check_visit(visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                return True
    return False

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
    
while True:
    gou = []

    while check_visit(visit):
        union=[]

        stack.append(give_not_visit(visit))
        make_un(stack)

        gou.append(union)

    if len(gou) == n*n:
        break

    def move(gou):
        for uns in gou:
            len_uns = len(uns)
            total = 0

            for con in uns:
                total += nations[con[0]][con[1]]

            res = total // len_uns

            for con in uns:
                nations[con[0]][con[1]] = res

    move(gou)

    cnt +=1
    visit = fast_copy(standard_v)

print(cnt)