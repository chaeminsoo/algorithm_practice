n = int(input())
m = int(input())
inf = 1e9
city =[[inf]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            city[i][j] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < city[a-1][b-1]:
        city[a-1][b-1] = c

for i in range(n):
    for a in range(n):
        for b in range(n):
            city[a][b] = min(city[a][b],city[a][i]+city[i][b])

for i in city:
    for j in i:
        if j == inf:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()