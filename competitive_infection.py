n,k = map(int,input().split())

virus = [[] for _ in range(k+1)]
field =[]

for i in range(n):
    data = list(map(int,input().split()))
    for d in range(len(data)):
        if data[d] != 0:
            virus[data[d]].append([i,d])
    field.append(data)

s, x, y = map(int,input().split())


def diffusion(r,c,v):
    global n, field
    new_virus=[]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]

        if new_r >= 0 and new_r < n and new_c >= 0 and new_c < n:
            if field[new_r][new_c] == 0:
                field[new_r][new_c] = v
                # new_virus.append([new_r,new_c])

