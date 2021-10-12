n,l,r = map(int,input().split())

A=[]
for i in range(n):
    row = list(map(int,input().split()))
    A.append(row)

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
unions = []
group_of_un =[]
dr=[-1,1,0,0]
dc=[0,0,-1,1]
check = True

def union():
    global visit,unions,group_of_un,stack
    try:
        r,c = stack.pop()
        unions.append([r,c])
    except IndexError:
        return

    visit[r][c] = 1
    standard = A[r][c]
    print(standard,'8888888888')
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nr < n and nc >= 0 and nc <n:
            print(A[nr][nc],'555555555555')
            print(abs(standard - A[nr][nc]),'44444444444444')
            if abs(standard - A[nr][nc]) >= l and abs(standard - A[nr][nc]) <= r:
                stack.append([nr,nc])
    union()

def move(unions):
    global A
    hab = 0
    lu = len(unions)
    if lu !=0:
        for i in range(lu):
            x,y = unions[i]
            hab += A[x][y]
        
        val = hab//lu

        while unions:
            w,z = unions.pop()
            A[w][z] = val
    
    return

result = 0
ref_a = []
switch = True
ref_a = fast_copy(A)
while switch:
    while True:
        coordinate = give_not_visit(visit)
        if coordinate == None:
            break
        stack.append(coordinate)
        union()
        print(unions)
        group_of_un.append(unions)
        unions=[]
    print(group_of_un)

    for uns in group_of_un:
        move(uns)
    print(A)

    if ref_a == A:
        switch = False
    else:
        ref_a = fast_copy(A)

    result+=1
    visit = fast_copy(standard_v)
    group_of_un = []

print(result)