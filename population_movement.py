n,l,r = map(int,input().split())

A=[]
for i in range(n):
    row = list(map(int,input().split()))
    A.append(row)

visit = [[0]*n for _ in range(n)]

def fast_copy(list):
    return [i[:] for i in list]

def give_not_visit(visit):
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                return [i,j]

stack = []
unions = []
group_of_un =[]
dr=[-1,1,0,0]
dc=[0,0,-1,1]
check = True

def union(stack):
    global visit,unions,group_of_un
    try:
        r,c = stack.pop()
        unions.append([r,c])
    except IndexError:
        group_of_un.append(unions)
        unions = []
        return

    visit[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >= 0 and nc <n:
            if abs(A[r][c] - A[nr][nc]) >= l and abs(A[r][c] - A[nr][nc]) <= r:
                stack.append([nr,nc])

    union(stack)

def move(unions):
    global A
    hab = 0
    lu = len(unions)
    for i in range(lu):
        x,y = unions[i]
        hab += A[x][y]
    
    val = hab//lu

    while unions:
        w,z = unions.pop()
        A[w][z] = val
    return

def gou():
    coordinate = give_not_visit(visit)
    if coordinate == None:
        return
    stack.append(coordinate)
    union(stack)

result = 0

while True:
    gou()

    

print(result)