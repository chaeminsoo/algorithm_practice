n,l,r = map(int,input().split())

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

stack = []
group_of_un =[]
unions = []
dr=[-1,1,0,0]
dc=[0,0,-1,1]
check = True

def union(stack):
    try:
        coordinate = stack.pop()
    except IndexError:
        return

    r = coordinate[0]
    c = coordinate[1]
    unions.append([r,c])
    visit[r][c] = 1
    
    ref = nations[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >=0 and nr <n and nc>=0 and nc < n:
            diff = nations[nr][nc] - ref
            if diff >= l and diff <= r:
                unions.append([nr,nc])
                stack.append([nr,nc])

    union(stack)

stack.append([0,0])
union(stack)

print(unions)