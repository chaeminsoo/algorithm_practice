n,L,R = map(int,input().split())

N = n*n
cnt = 0
nations=[]
for _ in range(n):
    nations.append(list(map(int,input().split())))

visit = [[0]*n for _ in range(n)]
stack=[]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def make_un(stack):
    union=[]
    total_sum = 0
    num_union = 0
    while stack:
        coordinate = stack.pop()
        
        union.append(coordinate)
        num_union += 1
        r,c = coordinate
        visit[r][c] = 1

        standard = nations[r][c]
        total_sum += standard

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                ref = nations[nr][nc]
                diff = abs(standard-ref)

                if diff >= L and diff <= R:
                    if visit[nr][nc] != 1:
                        stack.append([nr,nc])
                        visit[nr][nc] = 1
    union.append(num_union)
    union.append(total_sum)
    return union
    
def move(gou):
    for uns in gou:
        total = uns.pop()
        len_uns = uns.pop()

        res = total // len_uns

        for con in uns:
            nations[con[0]][con[1]] = res

while True:
    gou = []
    for i in range(n):
        for j in range(n):
            if visit[i][j] != 1:
                stack.append([i,j])
                gou.append(make_un(stack))
    if len(gou) == N:
        break

    move(gou)

    cnt +=1
    visit = [[0]*n for _ in range(n)]
    
print(cnt)